//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvghelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qdebug.h>

//  QSvgRectF::QSvgRectF(const QRectF &r, QtSvg::UnitTypes unitX,
//      QtSvg::UnitTypes unitY, QtSvg::UnitTypes unitW, QtSvg::UnitTypes
//      unitH)
extern "C" Q_DECL_EXPORT
QSvgRectF *ritual_ZN9QSvgRectFC1ERK6QRectFN5QtSvg9UnitTypesES4_S4_S4_(
    const QRectF *r,
    QtSvg::UnitTypes unitX,
    QtSvg::UnitTypes unitY,
    QtSvg::UnitTypes unitW,
    QtSvg::UnitTypes unitH) {
  return new QSvgRectF(*r, unitX, unitY, unitW, unitH);
}

//  QPointF QSvgRectF::translationRelativeToBoundingBox(const QRectF
//      &boundingBox) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QSvgRectF32translationRelativeToBoundingBoxERK6QRectF(
    const QSvgRectF *self,
    const QRectF *boundingBox) {
  return new QPointF(self->translationRelativeToBoundingBox(*boundingBox));
}

//  QRectF QSvgRectF::resolveRelativeLengths(const QRectF &localRect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QSvgRectF22resolveRelativeLengthsERK6QRectF(
    const QSvgRectF *self,
    const QRectF *localRect) {
  return new QRectF(self->resolveRelativeLengths(*localRect));
}

//  QRectF QSvgRectF::resolveRelativeLengths(const QRectF &localRect,
//      QtSvg::UnitTypes units) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QSvgRectF22resolveRelativeLengthsERK6QRectFN5QtSvg9UnitTypesE(
    const QSvgRectF *self,
    const QRectF *localRect,
    QtSvg::UnitTypes units) {
  return new QRectF(self->resolveRelativeLengths(*localRect, units));
}

//  QtSvg::UnitTypes QSvgRectF::unitX() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK9QSvgRectF5unitXEv(const QSvgRectF *self) {
  return self->unitX();
}

//  QtSvg::UnitTypes QSvgRectF::unitY() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK9QSvgRectF5unitYEv(const QSvgRectF *self) {
  return self->unitY();
}

//  QtSvg::UnitTypes QSvgRectF::unitW() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK9QSvgRectF5unitWEv(const QSvgRectF *self) {
  return self->unitW();
}

//  QtSvg::UnitTypes QSvgRectF::unitH() const
extern "C" Q_DECL_EXPORT
QtSvg::UnitTypes ritual_ZNK9QSvgRectF5unitHEv(const QSvgRectF *self) {
  return self->unitH();
}

//  void QSvgRectF::setUnitX(QtSvg::UnitTypes unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgRectF8setUnitXEN5QtSvg9UnitTypesE(
    QSvgRectF *self,
    QtSvg::UnitTypes unit) {
  self->setUnitX(unit);
}

//  void QSvgRectF::setUnitY(QtSvg::UnitTypes unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgRectF8setUnitYEN5QtSvg9UnitTypesE(
    QSvgRectF *self,
    QtSvg::UnitTypes unit) {
  self->setUnitY(unit);
}

//  void QSvgRectF::setUnitW(QtSvg::UnitTypes unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgRectF8setUnitWEN5QtSvg9UnitTypesE(
    QSvgRectF *self,
    QtSvg::UnitTypes unit) {
  self->setUnitW(unit);
}

//  void QSvgRectF::setUnitH(QtSvg::UnitTypes unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgRectF8setUnitHEN5QtSvg9UnitTypesE(
    QSvgRectF *self,
    QtSvg::UnitTypes unit) {
  self->setUnitH(unit);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QSvgRectF &r)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK9QSvgRectF(
    const QDebug *debug,
    const QSvgRectF *r) {
  return new QDebug(operator<<(*debug, *r));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QSvgRectF::~QSvgRectF()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSvgRectFD1Ev(QSvgRectF *self) {
  delete self;
}
