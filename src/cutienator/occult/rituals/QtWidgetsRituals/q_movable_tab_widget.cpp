//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qtabbar_p.h>
#include <QtGui/qpixmap.h>
#include "private/qlayoutengine_p.h"
#if QT_CONFIG(itemviews)
#include "qabstractitemdelegate.h"
#endif
#include "qapplication.h"
#include "qevent.h"
#include "qpainter.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qstylepainter.h"
#if QT_CONFIG(tabwidget)
#include "qtabwidget.h"
#endif
#if QT_CONFIG(tooltip)
#include "qtooltip.h"
#endif
#if QT_CONFIG(whatsthis)
#include "qwhatsthis.h"
#endif
#include "private/qtextengine_p.h"
#if QT_CONFIG(accessibility)
#include "qaccessible.h"
#endif
#ifdef Q_OS_MACOS
#include <qpa/qplatformnativeinterface.h>
#endif
#include "qmainwindow.h"
#include "private/qmainwindowlayout_p.h"
#include "qdebug.h"
#include "private/qapplication_p.h"
#include "private/qtabbar_p.h"

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/widgets/qtabbar.cpp, line 68, as _ZN17QMovableTabWidgetC1EP7QWidget
inline QMovableTabWidget::QMovableTabWidget(QWidget *parent)
    : QWidget(parent)
{
}

//  from src/widgets/widgets/qtabbar.cpp, line 73, as _ZN17QMovableTabWidget9setPixmapERK7QPixmap
inline void QMovableTabWidget::setPixmap(const QPixmap &pixmap)
{
    m_pixmap = pixmap;
    update();
}

//  from src/widgets/widgets/qtabbar.cpp, line 79, as _ZN17QMovableTabWidget10paintEventEP11QPaintEvent
inline void QMovableTabWidget::paintEvent(QPaintEvent *e)
{
    Q_UNUSED(e);
    QPainter p(this);
    p.drawPixmap(0, 0, m_pixmap);
}
//  -----------------------------------------------------------------------

//  Only a class built on QMovableTabWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMovableTabWidget : QMovableTabWidget {
  using QMovableTabWidget::paintEvent;
};

//  QMovableTabWidget::QMovableTabWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QMovableTabWidget *ritual_ZN17QMovableTabWidgetC1EP7QWidget(
    QWidget *parent) {
  return new QMovableTabWidget(parent);
}

//  void QMovableTabWidget::setPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMovableTabWidget9setPixmapERK7QPixmap(
    QMovableTabWidget *self,
    const QPixmap *pixmap) {
  self->setPixmap(*pixmap);
}

//  void QMovableTabWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMovableTabWidget10paintEventEP11QPaintEvent(
    QMovableTabWidget *self,
    QPaintEvent *e) {
  self->paintEvent(e);
}

//  void QMovableTabWidget::paintEvent(QPaintEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QMovableTabWidget10paintEventEP11QPaintEvent(
    QMovableTabWidget *self,
    QPaintEvent *e) {
  static_cast<OwnQMovableTabWidget *>(self)->OwnQMovableTabWidget::paintEvent(
      e);
}
