//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeolocation_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeolocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeolocation.h>
#include <QtPositioning/private/qgeolocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeolocation.cpp, line 12, as _ZN19QGeoLocationPrivateC1Ev
inline QGeoLocationPrivate::QGeoLocationPrivate()
    : QSharedData()
{
}

//  from ../qtpositioning/src/positioning/qgeolocation.cpp, line 17, as _ZN19QGeoLocationPrivateC1ERKS_
inline QGeoLocationPrivate::QGeoLocationPrivate(const QGeoLocationPrivate &other)
    : QSharedData()
{
    this->address = other.address;
    this->coordinate = other.coordinate;
    this->viewport = other.viewport;
    this->extendedAttributes = other.extendedAttributes;
}

//  from ../qtpositioning/src/positioning/qgeolocation.cpp, line 26, as _ZN19QGeoLocationPrivateD1Ev
inline QGeoLocationPrivate::~QGeoLocationPrivate()
{
}

//  from ../qtpositioning/src/positioning/qgeolocation.cpp, line 30, as _ZNK19QGeoLocationPrivateeqERKS_
inline bool QGeoLocationPrivate::operator==(const QGeoLocationPrivate &other) const
{
    return  (this->address == other.address
            && this->coordinate == other.coordinate
            && this->viewport == other.viewport
            && this->extendedAttributes == other.extendedAttributes);

}

//  from ../qtpositioning/src/positioning/qgeolocation.cpp, line 39, as _ZNK19QGeoLocationPrivate7isEmptyEv
inline bool QGeoLocationPrivate::isEmpty() const
{
    return (address.isEmpty()
            && !coordinate.isValid()
            && viewport.isEmpty()
            && extendedAttributes.isEmpty());
}
//  -----------------------------------------------------------------------

//  QGeoLocationPrivate::QGeoLocationPrivate()
extern "C" Q_DECL_EXPORT
QGeoLocationPrivate *ritual_ZN19QGeoLocationPrivateC1Ev() {
  return new QGeoLocationPrivate();
}

//  QGeoLocationPrivate::QGeoLocationPrivate(const QGeoLocationPrivate
//      &other)
extern "C" Q_DECL_EXPORT
QGeoLocationPrivate *ritual_ZN19QGeoLocationPrivateC1ERKS_(
    const QGeoLocationPrivate *other) {
  return new QGeoLocationPrivate(*other);
}

//  QGeoLocationPrivate::~QGeoLocationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoLocationPrivateD1Ev(QGeoLocationPrivate *self) {
  delete self;
}

//  bool QGeoLocationPrivate::operator==(const QGeoLocationPrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoLocationPrivateeqERKS_(
    const QGeoLocationPrivate *self,
    const QGeoLocationPrivate *other) {
  return self->operator==(*other);
}

//  bool QGeoLocationPrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoLocationPrivate7isEmptyEv(
    const QGeoLocationPrivate *self) {
  return self->isEmpty();
}
