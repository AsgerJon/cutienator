//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfu
//  siondial_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQuickControls2FusionStyleImpl/QtQuickControls2FusionStyleImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FusionStyleImpl/6.12.0/QtQuickControls2FusionStyleImpl/private/qquickfusiondial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2FusionStyleImpl/private/qquickfusiondial_p.h>
#include <QtGui/qpainter.h>
#include <QtGui/private/qmath_p.h>
#include <QtQuick/private/qquickpalette_p.h>
#include <QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 19, as _ZNK16QQuickFusionDial9highlightEv
inline bool QQuickFusionDial::highlight() const
{
    return m_highlight;
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 24, as _ZN16QQuickFusionDial12setHighlightEb
inline void QQuickFusionDial::setHighlight(bool highlight)
{
    if (m_highlight == highlight)
        return;

    m_highlight = highlight;
    update();
}

//  from ../qtdeclarative/src/quickcontrols/fusion/impl/qquickfusiondial.cpp, line 34, as _ZN16QQuickFusionDial5paintEP8QPainter
inline void QQuickFusionDial::paint(QPainter *painter)
{
    const int width = QQuickItem::width();
    const int height = QQuickItem::height();
    if (width <= 0 || height <= 0 || !isVisible())
        return;

    const bool enabled = isEnabled();
    qreal r = qMin(width, height) / 2.0;
    r -= r/50;
    const qreal penSize = r/20.0;

    painter->setRenderHint(QPainter::Antialiasing);

    const qreal d_ = r / 6;
    const qreal dx = d_ + (width - 2 * r) / 2 + 1;
    const qreal dy = d_ + (height - 2 * r) / 2 + 1;

    QRectF br = QRectF(dx + 0.5, dy + 0.5,
                       int(r * 2 - 2 * d_ - 2),
                       int(r * 2 - 2 * d_ - 2));
    QColor buttonColor = QQuickItemPrivate::get(this)->palette()->button().toHsv();
    buttonColor.setHsv(buttonColor .hue(),
                       qMin(140, buttonColor .saturation()),
                       qMax(180, buttonColor.value()));

    if (enabled) {
        // Drop shadow
        qreal shadowSize = qMax(1.0, penSize/2.0);
        QRectF shadowRect= br.adjusted(-2*shadowSize, -2*shadowSize,
                                       2*shadowSize, 2*shadowSize);
        QRadialGradient shadowGradient(shadowRect.center().x(),
                                       shadowRect.center().y(), shadowRect.width()/2.0,
                                       shadowRect.center().x(), shadowRect.center().y());
        shadowGradient.setColorAt(qreal(0.91), QColor(0, 0, 0, 40));
        shadowGradient.setColorAt(qreal(1.0), Qt::transparent);
        painter->setBrush(shadowGradient);
        painter->setPen(Qt::NoPen);
        painter->translate(shadowSize, shadowSize);
        painter->drawEllipse(shadowRect);
        painter->translate(-shadowSize, -shadowSize);

        // Main gradient
        QRadialGradient gradient(br.center().x() - br.width()/3, dy,
                                 br.width()*1.3, br.center().x(),
                                 br.center().y() - br.height()/2);
        gradient.setColorAt(0, buttonColor.lighter(110));
        gradient.setColorAt(qreal(0.5), buttonColor);
        gradient.setColorAt(qreal(0.501), buttonColor.darker(102));
        gradient.setColorAt(1, buttonColor.darker(115));
        painter->setBrush(gradient);
    } else {
        painter->setBrush(Qt::NoBrush);
    }

    painter->setPen(QPen(buttonColor.darker(280)));
    painter->drawEllipse(br);
    painter->setBrush(Qt::NoBrush);
    painter->setPen(buttonColor.lighter(110));
    painter->drawEllipse(br.adjusted(1, 1, -1, -1));

    if (m_highlight) {
        QColor highlight = QQuickItemPrivate::get(this)->palette()->highlight().toHsv();
        highlight.setHsv(highlight.hue(),
                         qMin(160, highlight.saturation()),
                         qMax(230, highlight.value()));
        highlight.setAlpha(127);
        painter->setPen(QPen(highlight, 2.0));
        painter->setBrush(Qt::NoBrush);
        painter->drawEllipse(br.adjusted(-1, -1, 1, 1));
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QQuickFusionDial::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickFusionDial10metaObjectEv(
    const QQuickFusionDial *self) {
  return self->metaObject();
}

//  bool QQuickFusionDial::highlight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuickFusionDial9highlightEv(const QQuickFusionDial *self) {
  return self->highlight();
}

//  void QQuickFusionDial::setHighlight(bool highlight)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFusionDial12setHighlightEb(
    QQuickFusionDial *self,
    bool highlight) {
  self->setHighlight(highlight);
}

//  void QQuickFusionDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickFusionDial5paintEP8QPainter(
    QQuickFusionDial *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QQuickFusionDial::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuickFusionDial5paintEP8QPainter(
    QQuickFusionDial *self,
    QPainter *painter) {
  self->QQuickFusionDial::paint(painter);
}
