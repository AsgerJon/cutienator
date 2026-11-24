//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(dockwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qdockarealayout_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qregion.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "QtWidgets/qapplication.h"
#include "QtWidgets/qwidget.h"
#if QT_CONFIG(tabbar)
#include "QtWidgets/qtabbar.h"
#endif
#include "QtWidgets/qstyle.h"
#include "QtWidgets/qapplication.h"
#include "QtCore/qvariant.h"
#include "qdockarealayout_p.h"
#include "qdockwidget.h"
#include "qmainwindow.h"
#include "qmainwindowlayout_p.h"
#include "qmenu_p.h"
#include "qdockwidget_p.h"
#include <private/qlayoutengine_p.h>
#if QT_CONFIG(toolbar)
#include "qtoolbar.h"
#include "qtoolbarlayout_p.h"
#endif
#include <qpainter.h>
#include <qstyleoption.h>
#include "qwidgetanimator_p.h"
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(mainwindow)
#include <private/qmainwindowlayout_p.h>
#endif
#include "qdockwidget.h"
#include <qaction.h>
#include <qapplication.h>
#if QT_CONFIG(accessibility)
#include <qaccessible.h>
#endif
#include <qdrawutil.h>
#include <qevent.h>
#include <qfontmetrics.h>
#include <qproxystyle.h>
#include <qwindow.h>
#include <qscreen.h>
#include <qmainwindow.h>
#include <qstylepainter.h>
#include <qtoolbutton.h>
#include <qdebug.h>
#include <private/qwidgetresizehandler_p.h>
#include <qpa/qplatformtheme.h>
#include <private/qhighdpiscaling_p.h>
#include "qdockwidget_p.h"
#include "qmainwindowlayout_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qdockarealayout.cpp, line 117, as _ZNK19QDockAreaLayoutItem11minimumSizeEv
inline QSize QDockAreaLayoutItem::minimumSize() const
{
    if (widgetItem)
        return widgetItem->minimumSize().grownBy(widgetItem->widget()->contentsMargins());
    if (subinfo != nullptr)
        return subinfo->minimumSize();
    return QSize(0, 0);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 96, as _ZNK19QDockAreaLayoutItem4skipEv
inline bool QDockAreaLayoutItem::skip() const
{
    if (placeHolderItem != nullptr)
        return true;

    if (flags & GapItem)
        return false;

    if (widgetItem != nullptr)
        return widgetItem->isEmpty();

    if (subinfo != nullptr) {
        for (int i = 0; i < subinfo->item_list.size(); ++i) {
            if (!subinfo->item_list.at(i).skip())
                return false;
        }
    }

    return true;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 126, as _ZNK19QDockAreaLayoutItem11maximumSizeEv
inline QSize QDockAreaLayoutItem::maximumSize() const
{
    if (widgetItem)
        return widgetItem->maximumSize().grownBy(widgetItem->widget()->contentsMargins());
    if (subinfo != nullptr)
        return subinfo->maximumSize();
    return QSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 135, as _ZNK19QDockAreaLayoutItem12hasFixedSizeEN2Qt11OrientationE
inline bool QDockAreaLayoutItem::hasFixedSize(Qt::Orientation o) const
{
    return perp(o, minimumSize()) == perp(o, maximumSize());
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 151, as _ZNK19QDockAreaLayoutItem8sizeHintEv
inline QSize QDockAreaLayoutItem::sizeHint() const
{
    if (placeHolderItem != nullptr)
        return QSize(0, 0);
    if (widgetItem)
        return widgetItem->sizeHint().grownBy(widgetItem->widget()->contentsMargins());
    if (subinfo != nullptr)
        return subinfo->sizeHint();
    return QSize(-1, -1);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 264, as _ZN19QDockAreaLayoutInfoC1EPKiN9QInternal12DockPositionEN2Qt11OrientationEiP11QMainWindow
inline QDockAreaLayoutInfo::QDockAreaLayoutInfo(const int *_sep, QInternal::DockPosition _dockPos,
                                            Qt::Orientation _o, int tbshape,
                                            QMainWindow *window)
    : sep(_sep), dockPos(_dockPos), o(_o), mainWindow(window)
#if QT_CONFIG(tabbar)
    , tabbed(false), tabBar(nullptr), tabBarShape(static_cast<QTabBar::Shape>(tbshape))
#endif
{
#if !QT_CONFIG(tabbar)
    Q_UNUSED(tbshape);
#endif
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 140, as _ZNK19QDockAreaLayoutItem9expansiveEN2Qt11OrientationE
inline bool QDockAreaLayoutItem::expansive(Qt::Orientation o) const
{
    if ((flags & GapItem) || placeHolderItem != nullptr)
        return false;
    if (widgetItem != nullptr)
        return ((widgetItem->expandingDirections() & o) == o);
    if (subinfo != nullptr)
        return subinfo->expansive(o);
    return false;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 90, as _ZN19QDockAreaLayoutItemD1Ev
inline QDockAreaLayoutItem::~QDockAreaLayoutItem()
{
    delete subinfo;
    delete placeHolderItem;
}

//  from src/widgets/widgets/qwidgetanimator.cpp, line 40, as _ZN15QWidgetAnimator7animateEP7QWidgetRK5QRectNS_13AnimationRuleE
inline void QWidgetAnimator::animate(QWidget *widget, const QRect &_final_geometry, AnimationRule rule)
{
    bool animate = rule == AnimationRule::Run;
    QRect r = widget->geometry();
    if (r.right() < 0 || r.bottom() < 0)
        r = QRect();

    animate = animate && !r.isNull() && !_final_geometry.isNull();

    // might make the widget go away by sending it to negative space
    const QRect final_geometry = _final_geometry.isValid() || widget->isWindow() ? _final_geometry :
        QRect(QPoint(-500 - widget->width(), -500 - widget->height()), widget->size());

#if QT_CONFIG(animation)
    //If the QStyle has animations, animate
    if (const int animationDuration = widget->style()->styleHint(QStyle::SH_Widget_Animation_Duration, nullptr, widget)) {
        AnimationMap::const_iterator it = m_animation_map.constFind(widget);
        if (it != m_animation_map.constEnd() && *it && (*it)->endValue().toRect() == final_geometry)
            return;

        QPropertyAnimation *anim = new QPropertyAnimation(widget, "geometry", widget);
        anim->setDuration(animate ? animationDuration : 0);
        anim->setEasingCurve(QEasingCurve::InOutQuad);
        anim->setEndValue(final_geometry);
        m_animation_map[widget] = anim;
        connect(anim, &QPropertyAnimation::destroyed, this, [this, widget]() { abort(widget); });
        anim->start(QPropertyAnimation::DeleteWhenStopped);
    } else
#endif // animation
    {
    //we do it in one shot
    widget->setGeometry(final_geometry);
#if QT_CONFIG(mainwindow)
    m_mainWindowLayout->animationFinished(widget);
#endif // QT_CONFIG(mainwindow)
    }
}

//  from src/widgets/widgets/qdockwidget.cpp, line 569, as _ZN15QDockWidgetItemC1EP11QDockWidget
inline QDockWidgetItem::QDockWidgetItem(QDockWidget *dockWidget)
    : QWidgetItem(dockWidget)
{
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 277, as _ZNK19QDockAreaLayoutInfo4sizeEv
inline QSize QDockAreaLayoutInfo::size() const
{
    return isEmpty() ? QSize(0, 0) : rect.size();
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1313, as _ZN19QDockAreaLayoutInfo4infoEP7QWidget
inline QDockAreaLayoutInfo *QDockAreaLayoutInfo::info(QWidget *widget)
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.skip())
            continue;

#if QT_CONFIG(tabbar)
        if (tabbed && widget == tabBar)
            return this;
#endif

        if (item.widgetItem != nullptr && item.widgetItem->widget() == widget)
            return this;

        if (item.subinfo != nullptr) {
            if (QDockAreaLayoutInfo *result = item.subinfo->info(widget))
                return result;
        }
    }

    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 505, as _ZNK19QDockAreaLayoutInfo9expansiveEN2Qt11OrientationE
inline bool QDockAreaLayoutInfo::expansive(Qt::Orientation o) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        if (item_list.at(i).expansive(o))
            return true;
    }
    return false;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1408, as _ZNK19QDockAreaLayoutInfo13separatorRectEi
inline QRect QDockAreaLayoutInfo::separatorRect(int index) const
{
#if QT_CONFIG(tabbar)
    if (tabbed)
        return QRect();
#endif

    const QDockAreaLayoutItem &item = item_list.at(index);
    if (item.skip())
        return QRect();

    QPoint pos = rect.topLeft();
    rpick(o, pos) = item.pos + item.size;
    QSize s = rect.size();
    rpick(o, s) = *sep;

    return QRect(pos, s);
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 282, as _ZN19QDockAreaLayoutInfo5clearEv
inline void QDockAreaLayoutInfo::clear()
{
    item_list.clear();
    rect = QRect();
#if QT_CONFIG(tabbar)
    tabbed = false;
    tabBar = nullptr;
#endif
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 292, as _ZNK19QDockAreaLayoutInfo7isEmptyEv
inline bool QDockAreaLayoutInfo::isEmpty() const
{
    return next(-1) == -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 297, as _ZNK19QDockAreaLayoutInfo19onlyHasPlaceholdersEv
inline bool QDockAreaLayoutInfo::onlyHasPlaceholders() const
{
    for (const QDockAreaLayoutItem &item : item_list) {
        if (!item.placeHolderItem)
            return false;
    }

    return true;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1719, as _ZNK19QDockAreaLayoutInfo4nextEi
inline int QDockAreaLayoutInfo::next(int index) const
{
    for (int i = index + 1; i < item_list.size(); ++i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1728, as _ZNK19QDockAreaLayoutInfo4prevEi
inline int QDockAreaLayoutInfo::prev(int index) const
{
    for (int i = index - 1; i >= 0; --i) {
        if (!item_list.at(i).skip())
            return i;
    }
    return -1;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1654, as _ZNK19QDockAreaLayoutInfo15separatorRegionEv
inline QRegion QDockAreaLayoutInfo::separatorRegion() const
{
    QRegion result;

    if (isEmpty())
        return result;
#if QT_CONFIG(tabbar)
    if (tabbed)
        return result;
#endif

    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);

        if (item.skip())
            continue;

        int next = this->next(i);

        if (item.subinfo)
            result |= item.subinfo->separatorRegion();

        if (next == -1)
            break;
        result |= separatorRect(i);
    }

    return result;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1788, as _ZNK19QDockAreaLayoutInfo6itemAtEPii
inline QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const
{
    for (int i = 0; i < item_list.size(); ++i) {
        const QDockAreaLayoutItem &item = item_list.at(i);
        if (item.placeHolderItem != nullptr)
            continue;
        if (item.subinfo) {
            if (QLayoutItem *ret = item.subinfo->itemAt(x, index))
                return ret;
        } else if (item.widgetItem) {
            if ((*x)++ == index)
                return item.widgetItem;
        }
    }
    return nullptr;
}

//  from src/widgets/widgets/qdockarealayout.cpp, line 1122, as _ZNK19QDockAreaLayoutInfo12currentTabIdEv
#if QT_CONFIG(tabbar)
inline quintptr QDockAreaLayoutInfo::currentTabId() const
{
    if (!tabbed || tabBar == nullptr)
        return 0;

    int index = tabBar->currentIndex();
    if (index == -1)
        return 0;

    return qvariant_cast<quintptr>(tabBar->tabData(index));
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1134, as _ZN19QDockAreaLayoutInfo13setCurrentTabEP7QWidget
#if QT_CONFIG(tabbar)
inline void QDockAreaLayoutInfo::setCurrentTab(QWidget *widget)
{
    setCurrentTabId(reinterpret_cast<quintptr>(widget));
}
#endif  // QT_CONFIG(tabbar)

//  from src/widgets/widgets/qdockarealayout.cpp, line 1139, as _ZN19QDockAreaLayoutInfo15setCurrentTabIdEy
#if QT_CONFIG(tabbar)
inline void QDockAreaLayoutInfo::setCurrentTabId(quintptr id)
{
    if (!tabbed || tabBar == nullptr)
        return;

    for (int i = 0; i < tabBar->count(); ++i) {
        if (qvariant_cast<quintptr>(tabBar->tabData(i)) == id) {
            tabBar->setCurrentIndex(i);
            return;
        }
    }
}
#endif  // QT_CONFIG(tabbar)
//  -----------------------------------------------------------------------

//  QSize QDockAreaLayoutInfo::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QDockAreaLayoutInfo4sizeEv(
    const QDockAreaLayoutInfo *self) {
  return new QSize(self->size());
}

//  QDockAreaLayoutInfo *QDockAreaLayoutInfo::info(QWidget *widget)
extern "C" Q_DECL_EXPORT
QDockAreaLayoutInfo *ritual_ZN19QDockAreaLayoutInfo4infoEP7QWidget(
    QDockAreaLayoutInfo *self,
    QWidget *widget) {
  return self->info(widget);
}

//  bool QDockAreaLayoutInfo::expansive(Qt::Orientation o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo9expansiveEN2Qt11OrientationE(
    const QDockAreaLayoutInfo *self,
    Qt::Orientation o) {
  return self->expansive(o);
}

//  QRect QDockAreaLayoutInfo::separatorRect(int index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QDockAreaLayoutInfo13separatorRectEi(
    const QDockAreaLayoutInfo *self,
    int index) {
  return new QRect(self->separatorRect(index));
}

//  void QDockAreaLayoutInfo::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfo5clearEv(QDockAreaLayoutInfo *self) {
  self->clear();
}

//  bool QDockAreaLayoutInfo::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo7isEmptyEv(
    const QDockAreaLayoutInfo *self) {
  return self->isEmpty();
}

//  bool QDockAreaLayoutInfo::onlyHasPlaceholders() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QDockAreaLayoutInfo19onlyHasPlaceholdersEv(
    const QDockAreaLayoutInfo *self) {
  return self->onlyHasPlaceholders();
}

//  int QDockAreaLayoutInfo::next(int idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDockAreaLayoutInfo4nextEi(
    const QDockAreaLayoutInfo *self,
    int idx) {
  return self->next(idx);
}

//  int QDockAreaLayoutInfo::prev(int idx) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QDockAreaLayoutInfo4prevEi(
    const QDockAreaLayoutInfo *self,
    int idx) {
  return self->prev(idx);
}

//  QRegion QDockAreaLayoutInfo::separatorRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK19QDockAreaLayoutInfo15separatorRegionEv(
    const QDockAreaLayoutInfo *self) {
  return new QRegion(self->separatorRegion());
}

//  QLayoutItem *QDockAreaLayoutInfo::itemAt(int *x, int index) const
extern "C" Q_DECL_EXPORT
QLayoutItem *ritual_ZNK19QDockAreaLayoutInfo6itemAtEPii(
    const QDockAreaLayoutInfo *self,
    int *x,
    int index) {
  return self->itemAt(x, index);
}

#if QT_CONFIG(tabbar)
//  quintptr QDockAreaLayoutInfo::currentTabId() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK19QDockAreaLayoutInfo12currentTabIdEv(
    const QDockAreaLayoutInfo *self) {
  return self->currentTabId();
}
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
//  void QDockAreaLayoutInfo::setCurrentTab(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfo13setCurrentTabEP7QWidget(
    QDockAreaLayoutInfo *self,
    QWidget *widget) {
  self->setCurrentTab(widget);
}
#endif  // QT_CONFIG(tabbar)

#if QT_CONFIG(tabbar)
//  void QDockAreaLayoutInfo::setCurrentTabId(quintptr id)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfo15setCurrentTabIdEy(
    QDockAreaLayoutInfo *self,
    quintptr id) {
  self->setCurrentTabId(id);
}
#endif  // QT_CONFIG(tabbar)

//  QDockAreaLayoutInfo::~QDockAreaLayoutInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDockAreaLayoutInfoD1Ev(QDockAreaLayoutInfo *self) {
  delete self;
}

#endif  // QT_CONFIG(dockwidget)
