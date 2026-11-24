//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/lecmaccalculator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/lecmaccalculator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/lecmaccalculator_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qcore_unix_p.h>
#include <cstring>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#ifdef CONFIG_LINUX_CRYPTO_API
#include <linux/if_alg.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/lecmaccalculator.cpp, line 49, as _ZN16LeCmacCalculatorD1Ev
inline LeCmacCalculator::~LeCmacCalculator()
{
    if (m_baseSocket != -1)
        close(m_baseSocket);
}
//  -----------------------------------------------------------------------

//  LeCmacCalculator::~LeCmacCalculator()
extern "C" Q_DECL_EXPORT
void ritual_ZN16LeCmacCalculatorD1Ev(LeCmacCalculator *self) {
  delete self;
}
