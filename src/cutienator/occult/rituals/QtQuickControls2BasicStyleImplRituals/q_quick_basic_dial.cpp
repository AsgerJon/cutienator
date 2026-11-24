//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasi
//  cdial_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2BasicStyleImpl/QtQuickControls2BasicStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2BasicStyleImpl/6.12.0/QtQuickControls2BasicStyleImpl/private/qquickbasicdial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickbasicdial_p.h"
#include <QtCore/qmath.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 19, as _ZNK15QQuickBasicDial8progressEv
inline qreal QQuickBasicDial::progress() const
{
    return m_progress;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 24, as _ZN15QQuickBasicDial11setProgressEd
inline void QQuickBasicDial::setProgress(qreal progress)
{
    if (progress == m_progress)
        return;

    m_progress = progress;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 33, as _ZNK15QQuickBasicDial10startAngleEv
inline qreal QQuickBasicDial::startAngle() const
{
    return m_startAngle;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 38, as _ZN15QQuickBasicDial13setStartAngleEd
inline void QQuickBasicDial::setStartAngle(qreal startAngle)
{
    if (startAngle == m_startAngle)
        return;

    m_startAngle = startAngle;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 47, as _ZNK15QQuickBasicDial8endAngleEv
inline qreal QQuickBasicDial::endAngle() const
{
    return m_endAngle;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 52, as _ZN15QQuickBasicDial11setEndAngleEd
inline void QQuickBasicDial::setEndAngle(qreal endAngle)
{
    if (endAngle == m_endAngle)
        return;

    m_endAngle = endAngle;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 61, as _ZNK15QQuickBasicDial5colorEv
inline QColor QQuickBasicDial::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 66, as _ZN15QQuickBasicDial8setColorERK6QColor
inline void QQuickBasicDial::setColor(const QColor &color)
{
    if (color == m_color)
        return;

    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/basic/impl/qquickbasicdial.cpp, line 75, as _ZN15QQuickBasicDial5paintEP8QPainter
inline void QQuickBasicDial::paint(QPainter *painter)
{
    if (width() <= 0 || height() <= 0)
        return;

    QPen pen(m_color);
    pen.setWidth(8);
    pen.setCapStyle(Qt::FlatCap);
    painter->setPen(pen);

    const QRectF bounds = boundingRect();
    const qreal smallest = qMin(bounds.width(), bounds.height());
    QRectF rect = QRectF(pen.widthF() / 2.0 + 1, pen.widthF() / 2.0 + 1, smallest - pen.widthF() - 2, smallest - pen.widthF() - 2);
    rect.moveCenter(bounds.center());

    // Make sure the arc is aligned to whole pixels.
    if (rect.x() - int(rect.x()) > 0)
        rect.setX(qCeil(rect.x()));
    if (rect.y() - int(rect.y()) > 0)
        rect.setY(qCeil(rect.y()));
    if (rect.width() - int(rect.width()) > 0)
        rect.setWidth(qFloor(rect.width()));
    if (rect.height() - int(rect.height()) > 0)
        rect.setHeight(qFloor(rect.height()));

    painter->setRenderHint(QPainter::Antialiasing);

    const qreal startAngle = 90. - m_startAngle;
    const qreal spanAngle = m_progress * (m_startAngle - m_endAngle);
    QPainterPath path;
    path.arcMoveTo(rect, startAngle);
    path.arcTo(rect, startAngle, spanAngle);
    painter->drawPath(path);

    rect.adjust(-pen.widthF() / 2.0, -pen.widthF() / 2.0, pen.widthF() / 2.0, pen.widthF() / 2.0);
    pen.setWidth(1);
    painter->setPen(pen);

    path = QPainterPath();
    path.arcMoveTo(rect, 0);
    path.arcTo(rect, 0, 360);
    painter->drawPath(path);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickBasicDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickBasicDial10metaObjectEv(
    const QQuickBasicDial *self) {
  return self->metaObject();
}

//  qreal QQuickBasicDial::progress() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickBasicDial8progressEv(const QQuickBasicDial *self) {
  return self->progress();
}

//  void QQuickBasicDial::setProgress(qreal progress)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial11setProgressEd(
    QQuickBasicDial *self,
    qreal progress) {
  self->setProgress(progress);
}

//  qreal QQuickBasicDial::startAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickBasicDial10startAngleEv(
    const QQuickBasicDial *self) {
  return self->startAngle();
}

//  void QQuickBasicDial::setStartAngle(qreal startAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial13setStartAngleEd(
    QQuickBasicDial *self,
    qreal startAngle) {
  self->setStartAngle(startAngle);
}

//  qreal QQuickBasicDial::endAngle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickBasicDial8endAngleEv(const QQuickBasicDial *self) {
  return self->endAngle();
}

//  void QQuickBasicDial::setEndAngle(qreal endAngle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial11setEndAngleEd(
    QQuickBasicDial *self,
    qreal endAngle) {
  self->setEndAngle(endAngle);
}

//  QColor QQuickBasicDial::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickBasicDial5colorEv(const QQuickBasicDial *self) {
  return new QColor(self->color());
}

//  void QQuickBasicDial::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial8setColorERK6QColor(
    QQuickBasicDial *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickBasicDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickBasicDial5paintEP8QPainter(
    QQuickBasicDial *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickBasicDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickBasicDial5paintEP8QPainter(
    QQuickBasicDial *self,
    QPainter *painter) {
  self->QQuickBasicDial::paint(painter);
}
