//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtoolbarextension_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qtoolbarextension_p.h>
#include <QtCore/qsize.h>
#include "qtoolbarextension_p.h"
#include <qevent.h>
#include <qstyle.h>
#include <qstylepainter.h>
#include <qstyleoption.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/widgets/qtoolbarextension.cpp, line 38, as _ZN17QToolBarExtension10paintEventEP11QPaintEvent
inline void QToolBarExtension::paintEvent(QPaintEvent *)
{
    QStylePainter p(this);
    QStyleOptionToolButton opt;
    initStyleOption(&opt);
    // We do not need to draw both extension arrows
    opt.features &= ~QStyleOptionToolButton::HasMenu;
    p.drawComplexControl(QStyle::CC_ToolButton, opt);
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 49, as _ZNK17QToolBarExtension8sizeHintEv
inline QSize QToolBarExtension::sizeHint() const
{
    QStyleOption opt;
    opt.initFrom(this);
    const int ext = style()->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, this);
    return QSize(ext, ext);
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 26, as _ZN17QToolBarExtension14setOrientationEN2Qt11OrientationE
inline void QToolBarExtension::setOrientation(Qt::Orientation o)
{
    QStyleOption opt;
    opt.initFrom(this);
    if (o == Qt::Horizontal) {
        setIcon(style()->standardIcon(QStyle::SP_ToolBarHorizontalExtensionButton, &opt, this));
    } else {
        setIcon(style()->standardIcon(QStyle::SP_ToolBarVerticalExtensionButton, &opt, this));
    }
    m_orientation = o;
}

//  from src/widgets/widgets/qtoolbarextension.cpp, line 57, as _ZN17QToolBarExtension5eventEP6QEvent
inline bool QToolBarExtension::event(QEvent *event)
{
    switch (event->type()) {
    case QEvent::LayoutDirectionChange:
        setOrientation(m_orientation);
        break;
    default:
        break;
    }
    return QToolButton::event(event);
}
//  -----------------------------------------------------------------------

//  Only a class built on QToolBarExtension may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQToolBarExtension : QToolBarExtension {
  using QToolBarExtension::event;
};

//  const QMetaObject *QToolBarExtension::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QToolBarExtension10metaObjectEv(
    const QToolBarExtension *self) {
  return self->metaObject();
}

//  void QToolBarExtension::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QToolBarExtension10paintEventEP11QPaintEvent(
    QToolBarExtension *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  QSize QToolBarExtension::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QToolBarExtension8sizeHintEv(
    const QToolBarExtension *self) {
  return new QSize(self->sizeHint());
}

//  void QToolBarExtension::setOrientation(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QToolBarExtension14setOrientationEN2Qt11OrientationE(
    QToolBarExtension *self,
    Qt::Orientation o) {
  self->setOrientation(o);
}

//  bool QToolBarExtension::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QToolBarExtension5eventEP6QEvent(
    QToolBarExtension *self,
    QEvent *e) {
  return self->event(e);
}

//  void QToolBarExtension::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QToolBarExtension10paintEventEP11QPaintEvent(
    QToolBarExtension *self,
    QPaintEvent *a0) {
  self->QToolBarExtension::paintEvent(a0);
}

//  QSize QToolBarExtension::sizeHint() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK17QToolBarExtension8sizeHintEv(
    const QToolBarExtension *self) {
  return new QSize(self->QToolBarExtension::sizeHint());
}

//  bool QToolBarExtension::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QToolBarExtension5eventEP6QEvent(
    QToolBarExtension *self,
    QEvent *e) {
  return static_cast<OwnQToolBarExtension *>(self)->OwnQToolBarExtension::event(
      e);
}
