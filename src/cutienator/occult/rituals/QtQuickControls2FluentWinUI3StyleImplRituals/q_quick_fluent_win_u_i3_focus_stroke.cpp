//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/priv
//  ate/qquickfluentwinui3focusstroke_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3styleimplglobal_p.h>
#include <QtQuickControls2FluentWinUI3StyleImpl/QtQuickControls2FluentWinUI3StyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FluentWinUI3StyleImpl/6.12.0/QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusstroke_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FluentWinUI3StyleImpl/private/qquickfluentwinui3focusstroke_p.h>
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

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 40, as _ZNK29QQuickFluentWinUI3FocusStroke6radiusEv
inline int QQuickFluentWinUI3FocusStroke::radius() const
{
    return m_radius;
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 44, as _ZN29QQuickFluentWinUI3FocusStroke9setRadiusEi
inline void QQuickFluentWinUI3FocusStroke::setRadius(int radius)
{
    if (m_radius == radius)
        return;
    m_radius = radius;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 29, as _ZNK29QQuickFluentWinUI3FocusStroke5colorEv
inline QColor QQuickFluentWinUI3FocusStroke::color() const
{
    return m_color;
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 33, as _ZN29QQuickFluentWinUI3FocusStroke8setColorERK6QColor
inline void QQuickFluentWinUI3FocusStroke::setColor(const QColor &color)
{
    if (color == m_color)
        return;
    m_color = color;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/fluentwinui3/impl/qquickfluentwinui3focusstroke.cpp, line 13, as _ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter
inline void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
{
    painter->setRenderHint(QPainter::Antialiasing);
    QPainterPath path;
    QRectF rect = boundingRect();
    path.moveTo(rect.left(), rect.top() + m_radius);
    path.lineTo(rect.left(), rect.bottom() - m_radius);
    path.arcTo(QRectF(rect.left(), rect.bottom() - 2 * m_radius, 2 * m_radius, 2 * m_radius), 180, 90);
    path.lineTo(rect.right() - m_radius, rect.bottom());
    path.arcTo(QRectF(rect.right() - 2 * m_radius, rect.bottom() - 2 * m_radius, 2 * m_radius, 2 * m_radius), 270, 90);
    path.lineTo(rect.right(), rect.top() + m_radius);
    path.lineTo(rect.right(), rect.top() + m_radius);
    path.lineTo(rect.right(), rect.top());
    path.lineTo(rect.left(), rect.top());
    painter->fillPath(path, m_color);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickFluentWinUI3FocusStroke::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickFluentWinUI3FocusStroke10metaObjectEv(
    const QQuickFluentWinUI3FocusStroke *self) {
  return self->metaObject();
}

//  int QQuickFluentWinUI3FocusStroke::radius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickFluentWinUI3FocusStroke6radiusEv(
    const QQuickFluentWinUI3FocusStroke *self) {
  return self->radius();
}

//  void QQuickFluentWinUI3FocusStroke::setRadius(int radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFluentWinUI3FocusStroke9setRadiusEi(
    QQuickFluentWinUI3FocusStroke *self,
    int radius) {
  self->setRadius(radius);
}

//  QColor QQuickFluentWinUI3FocusStroke::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK29QQuickFluentWinUI3FocusStroke5colorEv(
    const QQuickFluentWinUI3FocusStroke *self) {
  return new QColor(self->color());
}

//  void QQuickFluentWinUI3FocusStroke::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFluentWinUI3FocusStroke8setColorERK6QColor(
    QQuickFluentWinUI3FocusStroke *self,
    const QColor *color) {
  self->setColor(*color);
}

//  void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter(
    QQuickFluentWinUI3FocusStroke *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickFluentWinUI3FocusStroke::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickFluentWinUI3FocusStroke5paintEP8QPainter(
    QQuickFluentWinUI3FocusStroke *self,
    QPainter *painter) {
  self->QQuickFluentWinUI3FocusStroke::paint(painter);
}
