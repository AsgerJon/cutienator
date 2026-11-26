//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcanframeprocessor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcanframeprocessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <optional>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/qcanbusframe.h>
#include <QtSerialBus/qcanframeprocessor.h>
#include <QtSerialBus/private/qcanframeprocessor_p.h>
#include <QtSerialBus/qcanmessagedescription.h>
#include <QtSerialBus/private/qcanmessagedescription_p.h>
#include <QtSerialBus/qcansignaldescription.h>
#include <QtSerialBus/private/qcansignaldescription_p.h>
#include <QtCore/QHash>
#include <QtCore/QMap>
#include <QtCore/QVariant>
#include <QtCore/QtEndian>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 31, as local:qcanframeprocessor.cpp:extractMaxBitNum
static quint16 extractMaxBitNum(quint16 startBit, quint16 bitLength, QSysInfo::Endian endian)
{
#ifdef USE_DBC_COMPATIBLE_BE_HANDLING
    if (endian == QSysInfo::Endian::LittleEndian) {
        return startBit + bitLength - 1;
    } else {
        const auto startByteNum = startBit / 8;
        const auto bitsInStartByte = startBit % 8 + 1;
        const auto leftBits = bitLength - bitsInStartByte;
        if (leftBits <= 0)
            return startBit; // so start bit is the largest

        const auto leftBytesRounded = (leftBits % 8 == 0) ? leftBits / 8 : leftBits / 8 + 1;
        return (startByteNum + leftBytesRounded + 1) * 8 - 1;
    }
#else
    return startBit + bitLength - 1;
#endif // USE_DBC_COMPATIBLE_BE_HANDLING
}

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 627, as local:qcanframeprocessor.cpp:extractValue
#if defined(USE_DBC_COMPATIBLE_BE_HANDLING)
template <typename T>
static QVariant extractValue(const unsigned char *data, const QCanSignalDescription &signalDesc)
{
    constexpr auto tBitLength = sizeof(T) * 8;
    const auto length = signalDesc.bitLength();
    if constexpr (std::is_floating_point_v<T>)
        Q_ASSERT(tBitLength == length);
    else
        Q_ASSERT(tBitLength >= length);
    const auto maxBytesToRead = (length % 8 == 0) ? length / 8 : length / 8 + 1;
    const auto start = signalDesc.startBit();
    T value = {};
    const bool isBigEndian = signalDesc.dataEndian() == QSysInfo::Endian::BigEndian;
    if (isBigEndian) {
        // Big Endian - start bit is MSB
        if (start % 8 == 7 && length % 8 == 0) {
            // The data is aligned at byte offset, we can simply memcpy
            memcpy(&value, &data[(start - 7) / 8], maxBytesToRead);
        } else {
            // Data is not aligned at byte offset, we need to do some bit
            // shifting. We cannot perform bit operations on float or double
            // types, so we convert the value to uchar *.
            // Because of how BE data is organized, the indices for reading
            // would not be continuous. If we want to extract BE data from the
            // middle 12 bits of a 2-byte payload, we will need to read bits 5-0
            // and 15-10:
            // _________________________________________________________________
            // |7      |6      |5(MSB) |4      |3      |2      |1      |0      |
            // -----------------------------------------------------------------
            // |15     |14     |13     |12     |11     |10(LSB)|9      |8      |
            // -----------------------------------------------------------------
            unsigned char *valueData = reinterpret_cast<unsigned char *>(&value);
            qsizetype bitIdx = start;
            for (qsizetype processedBits = 0; processedBits < length; ++processedBits) {
                const auto dataByteIdx = bitIdx / 8;
                const auto dataBitIdx = bitIdx % 8;
                if (data[dataByteIdx] & (0x01 << dataBitIdx)) {
                    const auto byteIdx = processedBits / 8;
                    // start filling each byte from MSB
                    const auto bitIdx = 7 - (processedBits % 8);
                    valueData[byteIdx] |= (0x01 << bitIdx);
                }
                // handle jump like 0 -> 15 from the example above
                if (bitIdx % 8 == 0)
                    bitIdx += 15;
                else
                    --bitIdx;
            }
        }
    } else {
        // Little Endian - start bit is LSB
        if (start % 8 == 0 && length % 8 == 0) {
            // The data is aligned at byte offset, we can simply memcpy
            memcpy(&value, &data[start / 8], maxBytesToRead);
        } else {
            // Data is not aligned at byte offset, we need to do some bit
            // shifting. We cannot perform bit operations on float or double
            // types, so we convert the value to uchar *.
            unsigned char *valueData = reinterpret_cast<unsigned char *>(&value);
            quint16 valueIdx = 0;
            for (auto i = start; i < start + length; ++i, ++valueIdx) {
                const auto byteIdx = i / 8;
                const auto bitIdx = i % 8;
                if (data[byteIdx] & (0x01 << bitIdx))
                    valueData[valueIdx / 8] |= 0x01 << (valueIdx % 8);
            }
        }
    }
    // check and convert endian
    T convertedValue = {};
    if (isBigEndian)
        convertedValue = qFromBigEndian(value);
    else
        convertedValue = qFromLittleEndian(value);
    const bool endianChanged = convertedValue != value;
    value = convertedValue;
    // for signed & unsigned fill the most significant bits with proper values
    if constexpr (std::is_integral_v<T>) {
        if (tBitLength > length) {
            if (endianChanged) {
                // After endian conversion we have unneeded bits in the end,
                // so we need to cut them
                value = value >> (tBitLength - length);
            }
            // value has more bits than we could actually read, so we need to
            // fill the most significant bits properly
            const auto dataFormat = signalDesc.dataFormat();
            if (dataFormat == QtCanBus::DataFormat::SignedInteger) {
                if (value & (0x01ULL << (length - 1))) {
                    // msb = 1 -> negative value, fill the rest with 1's
                    for (auto i = length; i < tBitLength; ++i)
                        value |= (0x01ULL << i);
                } else {
                    // msb = 0 -> positive value, fill the rest with 0's
                    for (auto i = length; i < tBitLength; ++i)
                        value &= ~(0x01ULL << i);
                }
            } else if (dataFormat == QtCanBus::DataFormat::UnsignedInteger) {
                // simply fill most significant bits with 0's
                for (auto i = length; i < tBitLength; ++i)
                    value &= ~(0x01ULL << i);
            }
        }
    }
    // perform value conversions, if needed
    if (needValueConversion(signalDesc))
        return QVariant::fromValue(convertFromCanValue(value, signalDesc));

    return QVariant::fromValue(value);
}
#endif  // defined(USE_DBC_COMPATIBLE_BE_HANDLING)

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 888, as local:qcanframeprocessor.cpp:encodeValue
#if defined(USE_DBC_COMPATIBLE_BE_HANDLING)
template <typename T>
static void encodeValue(unsigned char *data, const QVariant &valueVar,
                        const QCanSignalDescription &signalDesc)
{
    constexpr auto tBitLength = sizeof(T) * 8;
    const auto length = signalDesc.bitLength();
    if constexpr (std::is_floating_point_v<T>)
        Q_ASSERT(tBitLength == length);
    else
        Q_ASSERT(tBitLength >= length);

    // Perform value conversion.
    T value = {};
    if (needValueConversion(signalDesc))
        value = static_cast<T>(std::round(convertToCanValue(valueVar, signalDesc)));
    else
        value = valueVar.value<T>();

    const bool dataLittleEndian = signalDesc.dataEndian() == QSysInfo::Endian::LittleEndian;

    const auto maxBytesToWrite = (length % 8 == 0) ? length / 8 : length / 8 + 1;

    // always treat the value-to-write as LE for simplicity
    value = qToLittleEndian(value);
    const quint16 start = signalDesc.startBit();
    if (dataLittleEndian) {
        // Little Endian
        if (start % 8 == 0 && length % 8 == 0) {
            // The data is aligned at byte offset, and has a round number of
            // bytes, so we can simply memcpy
            memcpy(&data[start / 8], &value, maxBytesToWrite);
        } else {
            const uchar *valueData = reinterpret_cast<const uchar *>(&value);
            for (quint16 i = 0; i < length; ++i) {
                const auto valueByteIdx = i / 8;
                const auto valueBitIdx = i % 8;
                const auto dataByteIdx = (start + i) / 8;
                const auto dataBitIdx = (start + i) % 8;

                if (valueData[valueByteIdx] & (0x01 << valueBitIdx))
                    data[dataByteIdx] |= (0x01 << dataBitIdx);
                else
                    data[dataByteIdx] &= ~(0x01 << dataBitIdx);
            }
        }
    } else {
        // Big Endian
        if (start % 8 == 7 && length % 8 == 0) {
            // The data is aligned at byte offset and has a round number of
            // bytes, so we can simply memcpy. Just need to convert to BE and
            // take the meaningful bytes (those will be the most significant
            // bytes after switching to BE).
            value = qToBigEndian(value);
            const uchar *valueData = reinterpret_cast<const uchar *>(&value);
            const auto byteIdx = sizeof(value) - maxBytesToWrite;
            memcpy(&data[(start - 7) / 8], &valueData[byteIdx], maxBytesToWrite);
        } else {
            // We need to start from the MSB of the valueToWrite
            // Because of how BE data is organized, the indices for writing
            // would not be continuous. If we want to write BE data to the
            // middle 12 bits of a 2-byte payload, we will need to write bits
            // 5-0 and 15-10:
            // _________________________________________________________________
            // |7      |6      |5(MSB) |4      |3      |2      |1      |0      |
            // -----------------------------------------------------------------
            // |15     |14     |13     |12     |11     |10(LSB)|9      |8      |
            // -----------------------------------------------------------------
            const uchar *valueData = reinterpret_cast<const uchar *>(&value);
            auto dataBit = signalDesc.startBit();
            for (auto valueBit = length - 1; valueBit >= 0; --valueBit) {
                const auto valueByteIdx = valueBit / 8;
                const auto valueBitIdx = valueBit % 8;
                const auto dataByteIdx = dataBit / 8;
                const auto dataBitIdx = dataBit % 8;
                if (valueData[valueByteIdx] & (0x01 << valueBitIdx))
                    data[dataByteIdx] |= (0x01 << dataBitIdx);
                else
                    data[dataByteIdx] &= ~(0x01 << dataBitIdx);
                // handle jumps like 0 -> 15
                if (dataBit % 8 == 0)
                    dataBit += 15;
                else
                    --dataBit;
            }
        }
    }
}
#endif  // defined(USE_DBC_COMPATIBLE_BE_HANDLING)

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 540, as _ZN25QCanFrameProcessorPrivate11resetErrorsEv
inline void QCanFrameProcessorPrivate::resetErrors()
{
    error = QCanFrameProcessor::Error::None;
    errorString.clear();
    warnings.clear();
}

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 547, as _ZN25QCanFrameProcessorPrivate8setErrorEN18QCanFrameProcessor5ErrorERK7QString
inline void QCanFrameProcessorPrivate::setError(QCanFrameProcessor::Error err, const QString &desc)
{
    error = err;
    errorString = desc;
}

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 553, as _ZN25QCanFrameProcessorPrivate10addWarningERK7QString
inline void QCanFrameProcessorPrivate::addWarning(const QString &warning)
{
    warnings.push_back(warning);
}

//  from ../qtserialbus/src/serialbus/qcanframeprocessor.cpp, line 1185, as _ZN25QCanFrameProcessorPrivate3getERK18QCanFrameProcessor
inline QCanFrameProcessorPrivate *QCanFrameProcessorPrivate::get(const QCanFrameProcessor &processor)
{
    return processor.d.get();
}
//  -----------------------------------------------------------------------

//  void QCanFrameProcessorPrivate::resetErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivate11resetErrorsEv(
    QCanFrameProcessorPrivate *self) {
  self->resetErrors();
}

//  void QCanFrameProcessorPrivate::setError(QCanFrameProcessor::Error err,
//      const QString &desc)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivate8setErrorEN18QCanFrameProcessor5ErrorERK7QString(
    QCanFrameProcessorPrivate *self,
    QCanFrameProcessor::Error err,
    const QString *desc) {
  self->setError(err, *desc);
}

//  void QCanFrameProcessorPrivate::addWarning(const QString &warning)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivate10addWarningERK7QString(
    QCanFrameProcessorPrivate *self,
    const QString *warning) {
  self->addWarning(*warning);
}

//  QCanFrameProcessorPrivate *QCanFrameProcessorPrivate::get(const
//      QCanFrameProcessor &processor)
extern "C" Q_DECL_EXPORT
QCanFrameProcessorPrivate *ritual_ZN25QCanFrameProcessorPrivate3getERK18QCanFrameProcessor(
    const QCanFrameProcessor *processor) {
  return QCanFrameProcessorPrivate::get(*processor);
}

//  QCanFrameProcessorPrivate::~QCanFrameProcessorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QCanFrameProcessorPrivateD1Ev(
    QCanFrameProcessorPrivate *self) {
  delete self;
}

//  a std::optional<QtCanBus::UniqueId> a ritual of QCanFrameProcessorPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCanFrameProcessorPrivate__std_optional_QtCanBus_UniqueId(
    std::optional<QtCanBus::UniqueId> *self) {
  delete self;
}
