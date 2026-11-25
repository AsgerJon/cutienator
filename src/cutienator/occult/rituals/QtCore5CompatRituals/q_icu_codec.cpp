//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/6.12.0/QtCore5Compat/private/qicucodec_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'availableCodecs' and 'aliases' are
//  left out, with the code taken for them, and so is the line pulling
//  in ICU's 'unicode/ucnv.h': they call ICU's 'ucnv_*', a library
//  outside Qt, whose names carry ICU's version, as
//  'ucnv_countAvailable_78'. Kept as it is when the generator runs
//  again.
#include <QtCore5Compat/qcore5global.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(icu) && QT_CONFIG(textcodec)
#if QT_CONFIG(textcodec)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore5Compat/QtCore5Compat>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/6.12.0/QtCore5Compat/private/qicucodec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore5Compat/private/qicucodec_p.h>
#include <QtCore5Compat/private/qtextcodec_p.h>
#include <QtCore5Compat/private/qutfcodec_p.h>
#include <QtCore5Compat/private/qlatincodec_p.h>
#include <QtCore5Compat/private/qsimplecodec_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(codecs)
#include <QtCore5Compat/private/qtsciicodec_p.h>
#include <QtCore5Compat/private/qisciicodec_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt5compat/src/core5/codecs/qicucodec.cpp, line 712, as _ZNK9QIcuCodec4nameEv
inline QByteArray QIcuCodec::name() const
{
    return m_name;
}

//  from ../qt5compat/src/core5/codecs/qicucodec.cpp, line 538, as _ZN9QIcuCodecD1Ev
inline QIcuCodec::~QIcuCodec()
{
}
//  -----------------------------------------------------------------------

//  QByteArray QIcuCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QIcuCodec4nameEv(const QIcuCodec *self) {
  return new QByteArray(self->name());
}

//  QIcuCodec::~QIcuCodec()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QIcuCodecD1Ev(QIcuCodec *self) {
  delete self;
}

//  QByteArray QIcuCodec::name() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK9QIcuCodec4nameEv(const QIcuCodec *self) {
  return new QByteArray(self->QIcuCodec::name());
}

#endif  // QT_CONFIG(textcodec)
#endif  // QT_CONFIG(icu) && QT_CONFIG(textcodec)
