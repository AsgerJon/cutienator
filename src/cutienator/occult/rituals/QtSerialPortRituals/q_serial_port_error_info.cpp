//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialPort/6.12.0/QtSerialPort/private/qserialport_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialPort/QtSerialPort>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialPort/6.12.0/QtSerialPort/private/qserialport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qserialport.h"
#include "qserialportinfo.h"
#include "qserialportinfo_p.h"
#include "qserialport_p.h"
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtserialport/src/serialport/qserialport.cpp, line 18, as _ZN20QSerialPortErrorInfoC1EN11QSerialPort15SerialPortErrorERK7QString
inline QSerialPortErrorInfo::QSerialPortErrorInfo(QSerialPort::SerialPortError newErrorCode,
                                           const QString &newErrorString)
    : errorCode(newErrorCode)
    , errorString(newErrorString)
{
    if (errorString.isNull()) {
        switch (errorCode) {
        case QSerialPort::NoError:
            errorString = QSerialPort::tr("No error");
            break;
        case QSerialPort::OpenError:
            errorString = QSerialPort::tr("Device is already open");
            break;
        case QSerialPort::NotOpenError:
            errorString = QSerialPort::tr("Device is not open");
            break;
        case QSerialPort::TimeoutError:
            errorString = QSerialPort::tr("Operation timed out");
            break;
        case QSerialPort::ReadError:
            errorString = QSerialPort::tr("Error reading from device");
            break;
        case QSerialPort::WriteError:
            errorString = QSerialPort::tr("Error writing to device");
            break;
        case QSerialPort::ResourceError:
            errorString = QSerialPort::tr("Device disappeared from the system");
            break;
        default:
            // an empty string will be interpreted as "Unknown error"
            // from the QIODevice::errorString()
            break;
        }
    }
}
//  -----------------------------------------------------------------------

//  QSerialPortErrorInfo::QSerialPortErrorInfo(QSerialPort::SerialPortError
//      newErrorCode, const QString &newErrorString)
extern "C" Q_DECL_EXPORT
QSerialPortErrorInfo *ritual_ZN20QSerialPortErrorInfoC1EN11QSerialPort15SerialPortErrorERK7QString(
    QSerialPort::SerialPortError newErrorCode,
    const QString *newErrorString) {
  return new QSerialPortErrorInfo(newErrorCode, *newErrorString);
}

//  QSerialPortErrorInfo::~QSerialPortErrorInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSerialPortErrorInfoD1Ev(QSerialPortErrorInfo *self) {
  delete self;
}
