//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qmodbusserver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qmodbusserver.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbusserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbuspdu.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qmodbuscommevent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qmodbusdeviceidentification.h>
#include <QtSerialBus/qmodbusserver.h>
#include <QtSerialBus/private/qmodbusserver_p.h>
#include <QtSerialBus/private/qmodbus_symbols_p.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qloggingcategory.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 649, as local:qmodbusserver.cpp:CHECK_SIZE_EQUALS
#define CHECK_SIZE_EQUALS(req) \

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 658, as local:qmodbusserver.cpp:CHECK_SIZE_LESS_THAN
#define CHECK_SIZE_LESS_THAN(req) \

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 757, as _ZN20QModbusServerPrivate11writeSingleERK10QModbusPduN15QModbusDataUnit12RegisterTypeE
inline QModbusResponse QModbusServerPrivate::writeSingle(const QModbusPdu &request,
                                                  QModbusDataUnit::RegisterType unitType)
{
    CHECK_SIZE_EQUALS(request);
    quint16 address = 0, value = 0xffff;
    request.decodeData(&address, &value);

    if ((unitType == QModbusDataUnit::Coils) && ((value != Coil::Off) && (value != Coil::On))) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    quint16 reg;   // Get the requested register, but deliberately ignore.
    if (!q_func()->data(unitType, address, &reg)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    if (!q_func()->setData(unitType, address, value)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }

    return QModbusResponse(request.functionCode(), address, value);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1131, as _ZN20QModbusServerPrivate27processReadFifoQueueRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadFifoQueueRequest(const QModbusRequest &request)
{
    CHECK_SIZE_LESS_THAN(request);
    quint16 address = 0;
    request.decodeData(&address);

    quint16 fifoCount;
    if (!q_func()->data(QModbusDataUnit::HoldingRegisters, address, &fifoCount)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    if (fifoCount > 31u) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    QModbusDataUnit fifoRegisters(QModbusDataUnit::HoldingRegisters, address + 1u, fifoCount);
    if (!q_func()->data(&fifoRegisters)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    return QModbusResponse(request.functionCode(), quint16((fifoCount * 2) + 2u), fifoCount,
                           fifoRegisters.values());
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1023, as _ZN20QModbusServerPrivate28processReportServerIdRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReportServerIdRequest(const QModbusRequest &request)
{
    CHECK_SIZE_EQUALS(request);

    Q_Q(QModbusServer);

    QByteArray data;
    QVariant tmp = q->value(QModbusServer::ServerIdentifier);
    if (tmp.isNull() || (!tmp.isValid())) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }
    data.append(tmp.value<quint8>());

    tmp = q->value(QModbusServer::RunIndicatorStatus);
    if (tmp.isNull() || (!tmp.isValid())) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }
    data.append(tmp.value<quint8>());

    tmp = q->value(QModbusServer::AdditionalData);
    if (!tmp.isNull() && tmp.isValid())
        data.append(tmp.toByteArray());

    data.prepend(data.size()); // byte count
    return QModbusResponse(request.functionCode(), data);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 907, as _ZN20QModbusServerPrivate29processGetCommEventLogRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processGetCommEventLogRequest(const QModbusRequest &request)
{
    CHECK_SIZE_EQUALS(request);
    const QVariant tmp = q_func()->value(QModbusServer::DeviceBusy);
    if (tmp.isNull() || (!tmp.isValid())) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }
    const quint16 deviceBusy = tmp.value<quint16>();

    QList<quint8> eventLog(int(m_commEventLog.size()));
    std::copy(m_commEventLog.cbegin(), m_commEventLog.cend(), eventLog.begin());

    // 6 -> 3 x 2 Bytes (Status, Event Count and Message Count)
    return QModbusResponse(request.functionCode(), quint8(eventLog.size() + 6), deviceBusy,
        m_counters[Counter::CommEvent], m_counters[Counter::BusMessage], eventLog);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1052, as _ZN20QModbusServerPrivate31processMaskWriteRegisterRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processMaskWriteRegisterRequest(const QModbusRequest &request)
{
    CHECK_SIZE_EQUALS(request);
    quint16 address = 0, andMask = 0xffff, orMask = 0;
    request.decodeData(&address, &andMask, &orMask);

    quint16 reg;
    if (!q_func()->data(QModbusDataUnit::HoldingRegisters, address, &reg)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    const quint16 result = (reg & andMask) | (orMask & (~ andMask));
    if (!q_func()->setData(QModbusDataUnit::HoldingRegisters, address, result)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }
    return QModbusResponse(request.functionCode(), request.data());
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 895, as _ZN20QModbusServerPrivate33processGetCommEventCounterRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processGetCommEventCounterRequest(const QModbusRequest &request)
{
    CHECK_SIZE_EQUALS(request);
    const QVariant tmp = q_func()->value(QModbusServer::DeviceBusy);
    if (tmp.isNull() || (!tmp.isValid())) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }
    const quint16 deviceBusy = tmp.value<quint16>();
    return QModbusResponse(request.functionCode(), deviceBusy, m_counters[Counter::CommEvent]);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 783, as _ZN20QModbusServerPrivate33processReadExceptionStatusRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadExceptionStatusRequest(const QModbusRequest &request)
{
    CHECK_SIZE_EQUALS(request);

    // Get the requested range out of the registers.
    const QVariant tmp = q_func()->value(QModbusServer::ExceptionStatusOffset);
    if (tmp.isNull() || (!tmp.isValid())) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }
    const quint16 exceptionStatusOffset = tmp.value<quint16>();
    QModbusDataUnit coils(QModbusDataUnit::Coils, exceptionStatusOffset, 8);
    if (!q_func()->data(&coils)) {
        return QModbusExceptionResponse(request.functionCode(),
                                        QModbusExceptionResponse::IllegalDataAddress);
    }

    qsizetype address = 0;
    quint8 byte = 0;
    for (int currentBit = 0; currentBit < 8; ++currentBit)
        if (coils.value(address++)) // The padding happens inside value().
            byte |= (1U << currentBit);

    return QModbusResponse(request.functionCode(), byte);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 977, as _ZN20QModbusServerPrivate36processWriteMultipleRegistersRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processWriteMultipleRegistersRequest(
    const QModbusRequest &request)
{
    CHECK_SIZE_LESS_THAN(request);
    quint16 address = 0, numberOfRegisters = 0;
    quint8 byteCount = 0;
    request.decodeData(&address, &numberOfRegisters, &byteCount);

    // byte count does not match number of data bytes following or register count
    if ((byteCount != (request.dataSize() - 5 )) || (byteCount != (numberOfRegisters * 2))) {
        return QModbusExceptionResponse(request.functionCode(),
                                        QModbusExceptionResponse::IllegalDataValue);
    }

    if ((numberOfRegisters < 0x0001) || (numberOfRegisters > 0x007B)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    // Get the requested range out of the registers.
    QModbusDataUnit registers(QModbusDataUnit::HoldingRegisters, address, numberOfRegisters);
    if (!q_func()->data(&registers)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    const QByteArray pduData = request.data().remove(0,5);
    QDataStream stream(pduData);

    QList<quint16> values;
    quint16 tmp;
    for (int i = 0; i < numberOfRegisters; i++) {
        stream >> tmp;
        values.append(tmp);
    }

    registers.setValues(values);

    if (!q_func()->setData(registers)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }

    return QModbusResponse(request.functionCode(), address, numberOfRegisters);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1072, as _ZN20QModbusServerPrivate40processReadWriteMultipleRegistersRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadWriteMultipleRegistersRequest(
    const QModbusRequest &request)
{
    CHECK_SIZE_LESS_THAN(request);
    quint16 readStartAddress = 0, readQuantity = 0, writeStartAddress = 0, writeQuantity = 0;
    quint8 byteCount = 0;
    request.decodeData(&readStartAddress, &readQuantity,
                       &writeStartAddress, &writeQuantity, &byteCount);

    // byte count does not match number of data bytes following or register count
    if ((byteCount != (request.dataSize() - 9 )) || (byteCount != (writeQuantity * 2))) {
        return QModbusExceptionResponse(request.functionCode(),
                                        QModbusExceptionResponse::IllegalDataValue);
    }

    if ((readQuantity < 0x0001) || (readQuantity > 0x007B)
            || (writeQuantity < 0x0001) || (writeQuantity > 0x0079)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    // According to spec, write operation is executed before the read operation
    // Get the requested range out of the registers.
    QModbusDataUnit writeRegisters(QModbusDataUnit::HoldingRegisters, writeStartAddress,
                                   writeQuantity);
    if (!q_func()->data(&writeRegisters)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    const QByteArray pduData = request.data().remove(0,9);
    QDataStream stream(pduData);

    QList<quint16> values;
    quint16 tmp;
    for (int i = 0; i < writeQuantity; i++) {
        stream >> tmp;
        values.append(tmp);
    }

    writeRegisters.setValues(values);

    if (!q_func()->setData(writeRegisters)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }

    // Get the requested range out of the registers.
    QModbusDataUnit readRegisters(QModbusDataUnit::HoldingRegisters, readStartAddress,
                                  readQuantity);
    if (!q_func()->data(&readRegisters)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    return QModbusResponse(request.functionCode(), quint8(readQuantity * 2),
                           readRegisters.values());
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1158, as _ZN20QModbusServerPrivate44processEncapsulatedInterfaceTransportRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processEncapsulatedInterfaceTransportRequest(
                                                                     const QModbusRequest &request)
{
    CHECK_SIZE_LESS_THAN(request);
    quint8 MEIType = 0;
    request.decodeData(&MEIType);

    switch (MEIType) {
        case EncapsulatedInterfaceTransport::CanOpenGeneralReference:
            break;
        case EncapsulatedInterfaceTransport::ReadDeviceIdentification: {
            if (request.dataSize() != 3u) {
                return QModbusExceptionResponse(request.functionCode(),
                    QModbusExceptionResponse::IllegalDataValue);
            }

            const QVariant tmp = q_func()->value(QModbusServer::DeviceIdentification);
            if (tmp.isNull() || (!tmp.isValid())) {
                // TODO: Is this correct?
                return QModbusExceptionResponse(request.functionCode(),
                    QModbusExceptionResponse::ServerDeviceFailure);
            }

            QModbusDeviceIdentification objectPool = tmp.value<QModbusDeviceIdentification>();
            if (!objectPool.isValid()) {
                // TODO: Is this correct?
                return QModbusExceptionResponse(request.functionCode(),
                    QModbusExceptionResponse::ServerDeviceFailure);
            }

            quint8 readDeviceIdCode = 0, objectId = 0;
            request.decodeData(&MEIType, &readDeviceIdCode, &objectId);
            if (!objectPool.contains(objectId)) {
                // Individual access requires the object Id to be present, so we will always fail.
                // For all other cases we will reevaluate object Id after we reset it as per spec.
                objectId = QModbusDeviceIdentification::VendorNameObjectId;
                if (readDeviceIdCode == QModbusDeviceIdentification::IndividualReadDeviceIdCode
                    || !objectPool.contains(objectId)) {
                    return QModbusExceptionResponse(request.functionCode(),
                        QModbusExceptionResponse::IllegalDataAddress);
                }
            }

            auto payload = [MEIType, readDeviceIdCode, objectId, objectPool](int lastObjectId) {
                // TODO: Take conformity level into account.
                QByteArray payload(6, Qt::Uninitialized);
                payload[0] = MEIType;
                payload[1] = readDeviceIdCode;
                payload[2] = quint8(objectPool.conformityLevel());
                payload[3] = quint8(0x00); // no more follows
                payload[4] = quint8(0x00); // next object id
                payload[5] = quint8(0x00); // number of objects

                const QList<int> objectIds = objectPool.objectIds();
                for (int id : objectIds) {
                    if (id < objectId)
                        continue;
                    if (id > lastObjectId)
                        break;
                    const QByteArray object = objectPool.value(id);
                    QByteArray objectData(2, Qt::Uninitialized);
                    objectData[0] = id;
                    objectData[1] = quint8(object.size());
                    objectData += object;
                    if (payload.size() + objectData.size() > 253) {
                        payload[3] = char(0xff); // more follows
                        payload[4] = id; // next object id
                        break;
                    }
                    payload.append(objectData);
                    payload[5] = payload[5] + 1u; // number of objects
                }
                return payload;
            };

            switch (readDeviceIdCode) {
            case QModbusDeviceIdentification::BasicReadDeviceIdCode:
                // TODO: How to handle a valid Id <> VendorName ... MajorMinorRevision
                return QModbusResponse(request.functionCode(),
                    payload(QModbusDeviceIdentification::MajorMinorRevisionObjectId));
            case QModbusDeviceIdentification::RegularReadDeviceIdCode:
                // TODO: How to handle a valid Id <> VendorUrl ... UserApplicationName
                return QModbusResponse(request.functionCode(),
                    payload(QModbusDeviceIdentification::UserApplicationNameObjectId));
            case QModbusDeviceIdentification::ExtendedReadDeviceIdCode:
                // TODO: How to handle a valid Id < ProductDependent
                return QModbusResponse(request.functionCode(),
                    payload(QModbusDeviceIdentification::UndefinedObjectId));
            case QModbusDeviceIdentification::IndividualReadDeviceIdCode: {
                // TODO: Take conformity level into account.
                const QByteArray object = objectPool.value(objectId);
                QByteArray header(8, Qt::Uninitialized);
                header[0] = MEIType;
                header[1] = readDeviceIdCode;
                header[2] = quint8(objectPool.conformityLevel());
                header[3] = quint8(0x00); // no more follows
                header[4] = quint8(0x00); // next object id
                header[5] = quint8(0x01); // number of objects
                header[6] = objectId;
                header[7] = quint8(object.size());
                return QModbusResponse(request.functionCode(), QByteArray(header + object));
            }
            default:
                return QModbusExceptionResponse(request.functionCode(),
                    QModbusExceptionResponse::IllegalDataValue);
            }
        }   break;
    }
    return QModbusExceptionResponse(request.functionCode(),
        QModbusExceptionResponse::IllegalFunction);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 725, as _ZN20QModbusServerPrivate9readBytesERK10QModbusPduN15QModbusDataUnit12RegisterTypeE
inline QModbusResponse QModbusServerPrivate::readBytes(const QModbusPdu &request,
                                                QModbusDataUnit::RegisterType unitType)
{
    CHECK_SIZE_EQUALS(request);
    quint16 address = 0, count = 0;
    request.decodeData(&address, &count);

    if ((count < 0x0001) || (count > 0x007D)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    // Get the requested range out of the registers.
    QModbusDataUnit unit(unitType, address, count);
    if (!q_func()->data(&unit)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    return QModbusResponse(request.functionCode(), quint8(count * 2), unit.values());
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 596, as _ZN20QModbusServerPrivate6setMapERK4QMapIN15QModbusDataUnit12RegisterTypeES1_E
inline bool QModbusServerPrivate::setMap(const QModbusDataUnitMap &map)
{
    m_modbusDataUnitMap = map;
    return true;
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 667, as _ZN20QModbusServerPrivate23processReadCoilsRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadCoilsRequest(const QModbusRequest &request)
{
    return readBits(request, QModbusDataUnit::Coils);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 672, as _ZN20QModbusServerPrivate32processReadDiscreteInputsRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadDiscreteInputsRequest(const QModbusRequest &rqst)
{
    return readBits(rqst, QModbusDataUnit::DiscreteInputs);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 677, as _ZN20QModbusServerPrivate8readBitsERK10QModbusPduN15QModbusDataUnit12RegisterTypeE
inline QModbusResponse QModbusServerPrivate::readBits(const QModbusPdu &request,
                                               QModbusDataUnit::RegisterType unitType)
{
    CHECK_SIZE_EQUALS(request);
    quint16 address = 0, count = 0;
    request.decodeData(&address, &count);

    if ((count < 0x0001) || (count > 0x07D0)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    // Get the requested range out of the registers.
    QModbusDataUnit unit(unitType, address, count);
    if (!q_func()->data(&unit)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    quint8 byteCount = quint8(count / 8);
    if ((count % 8) != 0) {
        byteCount += 1;
        // If the range is not a multiple of 8, resize.
        unit.setValueCount(byteCount * 8);
    }

    // Using byteCount * 8 so the remaining bits in the last byte are zero
    QBitArray bytes(byteCount * 8);

    address = 0; // The data range now starts with zero.
    for ( ; address < count; ++address)
        bytes.setBit(address, unit.value(address));

    QByteArray payload = QByteArray::fromRawData(bytes.bits(), byteCount);
    payload.prepend(char(byteCount));
    return QModbusResponse(request.functionCode(), payload);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 715, as _ZN20QModbusServerPrivate34processReadHoldingRegistersRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadHoldingRegistersRequest(const QModbusRequest &rqst)
{
    return readBytes(rqst, QModbusDataUnit::HoldingRegisters);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 720, as _ZN20QModbusServerPrivate32processReadInputRegistersRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processReadInputRegistersRequest(const QModbusRequest &rqst)
{
    return readBytes(rqst, QModbusDataUnit::InputRegisters);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 747, as _ZN20QModbusServerPrivate29processWriteSingleCoilRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processWriteSingleCoilRequest(const QModbusRequest &request)
{
    return writeSingle(request, QModbusDataUnit::Coils);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 752, as _ZN20QModbusServerPrivate33processWriteSingleRegisterRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processWriteSingleRegisterRequest(const QModbusRequest &rqst)
{
    return writeSingle(rqst, QModbusDataUnit::HoldingRegisters);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 925, as _ZN20QModbusServerPrivate32processWriteMultipleCoilsRequestERK14QModbusRequest
inline QModbusResponse QModbusServerPrivate::processWriteMultipleCoilsRequest(const QModbusRequest &request)
{
    CHECK_SIZE_LESS_THAN(request);
    quint16 address = 0, numberOfCoils = 0;
    quint8 byteCount = 0;
    request.decodeData(&address, &numberOfCoils, &byteCount);

    // byte count does not match number of data bytes following
    if (byteCount != (request.dataSize() - 5 )) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    quint8 expectedBytes = numberOfCoils / 8;
    if ((numberOfCoils % 8) != 0)
        expectedBytes += 1;

    if ((numberOfCoils < 0x0001) || (numberOfCoils > 0x07B0) || (expectedBytes != byteCount)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataValue);
    }

    // Get the requested range out of the registers.
    QModbusDataUnit coils(QModbusDataUnit::Coils, address, numberOfCoils);
    if (!q_func()->data(&coils)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::IllegalDataAddress);
    }

    QList<quint8> bytes;
    const QByteArray payload = request.data().mid(5);
    for (qint32 i = payload.size() - 1; i >= 0; --i)
        bytes.append(quint8(payload[i]));

    // Since we picked the coils at start address, data
    // range is numberOfCoils and therefore index too.
    quint16 coil = numberOfCoils;
    qint32 currentBit = 8 - ((byteCount * 8) - numberOfCoils);
    for (quint8 currentByte : std::as_const(bytes)) {
        for (currentBit -= 1; currentBit >= 0; --currentBit)
            coils.setValue(--coil, currentByte & (1U << currentBit) ? 1 : 0);
        currentBit = 8;
    }

    if (!q_func()->setData(coils)) {
        return QModbusExceptionResponse(request.functionCode(),
            QModbusExceptionResponse::ServerDeviceFailure);
    }

    return QModbusResponse(request.functionCode(), address, numberOfCoils);
}

//  from ../qtserialbus/src/serialbus/qmodbusserver.cpp, line 1270, as _ZN20QModbusServerPrivate20storeModbusCommEventERK16QModbusCommEvent
inline void QModbusServerPrivate::storeModbusCommEvent(const QModbusCommEvent &eventByte)
{
    // Inserts an event byte at the start of the event log. If the event log
    // is already full, the byte at the end of the log will be removed. The
    // event log size is 64 bytes, starting at index 0.
    m_commEventLog.push_front(eventByte);
    if (m_commEventLog.size() > 64)
        m_commEventLog.pop_back();
}
//  -----------------------------------------------------------------------

//  A QModbusServerPrivate that Python can take functions over in. Every QModbusServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQModbusServerPrivateCall0)(const void *, int *);
class CuteQModbusServerPrivate : public QModbusServerPrivate {
public:
  using QModbusServerPrivate::QModbusServerPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QModbusDevicePrivate6deviceEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QIODevice *QModbusDevicePrivate::device() const
  QIODevice *device() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQModbusServerPrivateCall0 call = reinterpret_cast<CuteQModbusServerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QModbusDevicePrivate::device();
  }
};

//  QModbusServer *QModbusServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QModbusServer *ritual_ZN20QModbusServerPrivate6q_funcEv(
    QModbusServerPrivate *self) {
  return self->q_func();
}

//  const QModbusServer *QModbusServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QModbusServer *ritual_ZNK20QModbusServerPrivate6q_funcEv(
    const QModbusServerPrivate *self) {
  return self->q_func();
}

//  QModbusServerPrivate::QModbusServerPrivate()
extern "C" Q_DECL_EXPORT
QModbusServerPrivate *ritual_ZN20QModbusServerPrivateC1Ev() {
  return new CuteQModbusServerPrivate();
}

//  bool QModbusServerPrivate::setMap(const QModbusDataUnitMap &map)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QModbusServerPrivate6setMapERK4QMapIN15QModbusDataUnit12RegisterTypeES1_E(
    QModbusServerPrivate *self,
    const QModbusDataUnitMap *map) {
  return self->setMap(*map);
}

//  void QModbusServerPrivate::resetCommunicationCounters()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusServerPrivate26resetCommunicationCountersEv(
    QModbusServerPrivate *self) {
  self->resetCommunicationCounters();
}

//  void QModbusServerPrivate::incrementCounter(QModbusServerPrivate::Counter
//      counter)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusServerPrivate16incrementCounterENS_7CounterE(
    QModbusServerPrivate *self,
    QModbusServerPrivate::Counter counter) {
  self->incrementCounter(counter);
}

//  QModbusResponse QModbusServerPrivate::processReadCoilsRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate23processReadCoilsRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(self->processReadCoilsRequest(*request));
}

//  QModbusResponse
//      QModbusServerPrivate::processReadDiscreteInputsRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate32processReadDiscreteInputsRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(
      self->processReadDiscreteInputsRequest(
          *request));
}

//  QModbusResponse QModbusServerPrivate::readBits(const QModbusPdu &request,
//      QModbusDataUnit::RegisterType unitType)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate8readBitsERK10QModbusPduN15QModbusDataUnit12RegisterTypeE(
    QModbusServerPrivate *self,
    const QModbusPdu *request,
    QModbusDataUnit::RegisterType unitType) {
  return new QModbusResponse(self->readBits(*request, unitType));
}

//  QModbusResponse
//      QModbusServerPrivate::processReadHoldingRegistersRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate34processReadHoldingRegistersRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(
      self->processReadHoldingRegistersRequest(
          *request));
}

//  QModbusResponse
//      QModbusServerPrivate::processReadInputRegistersRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate32processReadInputRegistersRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(
      self->processReadInputRegistersRequest(
          *request));
}

//  QModbusResponse QModbusServerPrivate::processWriteSingleCoilRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate29processWriteSingleCoilRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(self->processWriteSingleCoilRequest(*request));
}

//  QModbusResponse
//      QModbusServerPrivate::processWriteSingleRegisterRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate33processWriteSingleRegisterRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(
      self->processWriteSingleRegisterRequest(
          *request));
}

//  QModbusResponse
//      QModbusServerPrivate::processWriteMultipleCoilsRequest(const
//      QModbusRequest &request)
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZN20QModbusServerPrivate32processWriteMultipleCoilsRequestERK14QModbusRequest(
    QModbusServerPrivate *self,
    const QModbusRequest *request) {
  return new QModbusResponse(
      self->processWriteMultipleCoilsRequest(
          *request));
}

//  void QModbusServerPrivate::storeModbusCommEvent(const QModbusCommEvent
//      &eventByte)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QModbusServerPrivate20storeModbusCommEventERK16QModbusCommEvent(
    QModbusServerPrivate *self,
    const QModbusCommEvent *eventByte) {
  self->storeModbusCommEvent(*eventByte);
}

//  a Python function taken by a CuteQModbusServerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusServerPrivate(
    QModbusServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusServerPrivate *>(self)->take(key, call);
}
