//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetanimator_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'QWidgetAnimator' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(dockwidget)
#include <QtWidgets/private/qdockarealayout_p.h>
#include <QtWidgets/qdockwidget.h>
#include <QtWidgets/private/qdockwidget_p.h>
#endif
#if QT_CONFIG(toolbar)
#include <QtWidgets/private/qtoolbar_p.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/private/qtoolbarlayout_p.h>
#endif
#include <QtWidgets/qmainwindow.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#if QT_CONFIG(tabbar)
#include <QtWidgets/private/qtabbar_p.h>
#endif
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtCore/qmimedata.h>
#if QT_CONFIG(statusbar)
#include <QtWidgets/qstatusbar.h>
#endif
#include <QtCore/qstring.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstylepainter.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qstack.h>
#include <QtCore/qmap.h>
#include <QtCore/qpointer.h>
#ifndef QT_NO_DEBUG_STREAM
#  include <QtCore/qdebug.h>
#  include <QtCore/qtextstream.h>
#endif
#include <QtWidgets/private/qmenu_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qlayoutengine_p.h>
#include <QtWidgets/private/qwidgetresizehandler_p.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtCore/QScopedValueRollback>
#include <QtCore/private/qoffsetstringarray_p.h>
#include <optional>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qaction.h>
#include <QtWidgets/qwidgetaction.h>
#include <QtWidgets/qtoolbar.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/qtoolbutton.h>
#endif
#include <QtWidgets/qmenu.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmath.h>
#ifdef Q_OS_MACOS
#include <QtGui/qpa/qplatformnativeinterface.h>
#endif
#include <QtWidgets/private/qmainwindowlayout_p.h>
#if QT_CONFIG(toolbutton)
#include <QtWidgets/private/qtoolbarextension_p.h>
#endif
#include <QtWidgets/private/qtoolbarlayout_p.h>
#include <QtWidgets/private/qtoolbarseparator_p.h>
#include <QtWidgets/private/qwidgetanimator_p.h>
#if QT_CONFIG(animation)
#include <QtCore/qpropertyanimation.h>
#endif
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(mainwindow)
#include <QtWidgets/private/qmainwindowlayout_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 308, as local:qtoolbarlayout.cpp:defaultWidgetAction
static bool defaultWidgetAction(QToolBarItem *item)
{
    QWidgetAction *a = qobject_cast<QWidgetAction*>(item->action);
    return a != nullptr && a->defaultWidget() == item->widget();
}

//  from QtWidgets__QWidgetAnimator.cpp, line 1, as moc:QWidgetAnimator
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15QWidgetAnimatorE_t {};
} // unnamed namespace

template <> constexpr inline auto QWidgetAnimator::qt_create_metaobjectdata<qt_meta_tag_ZN15QWidgetAnimatorE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "QWidgetAnimator",
        "AnimationRule",
        "Run",
        "Stop"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
        // enum 'AnimationRule'
        QtMocHelpers::EnumData<enum AnimationRule>(1, 1, QMC::EnumIsScoped).add({
            {    2, AnimationRule::Run },
            {    3, AnimationRule::Stop },
        }),
    };
    return QtMocHelpers::metaObjectData<QWidgetAnimator, qt_meta_tag_ZN15QWidgetAnimatorE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject QWidgetAnimator::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QWidgetAnimatorE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QWidgetAnimatorE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15QWidgetAnimatorE_t>.metaTypes,
    nullptr
} };

void QWidgetAnimator::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<QWidgetAnimator *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *QWidgetAnimator::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *QWidgetAnimator::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15QWidgetAnimatorE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int QWidgetAnimator::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from src/widgets/widgets/qmainwindowlayout.cpp, line 2749, as _ZN17QMainWindowLayout17animationFinishedEP7QWidget
inline void QMainWindowLayout::animationFinished(QWidget *widget)
{
    //this function is called from within the Widget Animator whenever an animation is finished
    //on a certain widget
#if QT_CONFIG(toolbar)
    if (QToolBar *tb = qobject_cast<QToolBar*>(widget)) {
        QToolBarLayout *tbl = qobject_cast<QToolBarLayout*>(tb->layout());
        if (tbl->animating) {
            tbl->animating = false;
            if (tbl->expanded)
                tbl->layoutActions(tb->size());
            tb->update();
        }
    }
#endif

    if (widget == pluggingWidget) {

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
        if (QDockWidgetGroupWindow *dwgw = qobject_cast<QDockWidgetGroupWindow *>(widget)) {
            // When the animated widget was a QDockWidgetGroupWindow, it means each of the
            // embedded QDockWidget needs to be plugged back into the QMainWindow layout.
            savedState.clear();
            QDockAreaLayoutInfo *srcInfo = dwgw->layoutInfo();
            const QDockAreaLayoutInfo *srcTabInfo = dwgw->tabLayoutInfo();
            QDockAreaLayoutInfo *dstParentInfo;
            QList<int> dstPath;

            if (currentHoveredFloat) {
                dstPath = currentHoveredFloat->layoutInfo()->indexOf(widget);
                Q_ASSERT(dstPath.size() >= 1);
                dstParentInfo = currentHoveredFloat->layoutInfo()->info(dstPath);
            } else {
                dstPath = layoutState.dockAreaLayout.indexOf(widget);
                Q_ASSERT(dstPath.size() >= 2);
                dstParentInfo = layoutState.dockAreaLayout.info(dstPath);
            }
            Q_ASSERT(dstParentInfo);
            int idx = dstPath.constLast();
            Q_ASSERT(dstParentInfo->item_list[idx].widgetItem->widget() == dwgw);
            if (dstParentInfo->tabbed && srcTabInfo) {
                // merge the two tab widgets
                delete dstParentInfo->item_list[idx].widgetItem;
                dstParentInfo->item_list.removeAt(idx);
                std::copy(srcTabInfo->item_list.cbegin(), srcTabInfo->item_list.cend(),
                          std::inserter(dstParentInfo->item_list,
                                        dstParentInfo->item_list.begin() + idx));
                quintptr currentId = srcTabInfo->currentTabId();
                *srcInfo = QDockAreaLayoutInfo();
                dstParentInfo->reparentWidgets(currentHoveredFloat ? currentHoveredFloat.data()
                                                                   : parentWidget());
                dstParentInfo->updateTabBar();
                dstParentInfo->setCurrentTabId(currentId);
            } else {
                QDockAreaLayoutItem &item = dstParentInfo->item_list[idx];
                Q_ASSERT(item.widgetItem->widget() == dwgw);
                delete item.widgetItem;
                item.widgetItem = nullptr;
                item.subinfo = new QDockAreaLayoutInfo(std::move(*srcInfo));
                *srcInfo = QDockAreaLayoutInfo();
                item.subinfo->reparentWidgets(currentHoveredFloat ? currentHoveredFloat.data()
                                                                  : parentWidget());
                item.subinfo->setTabBarShape(dstParentInfo->tabBarShape);
            }
            dwgw->destroyOrHideIfEmpty();
        }
#endif

        if (QDockWidget *dw = qobject_cast<QDockWidget*>(widget)) {
            dw->setParent(currentHoveredFloat ? currentHoveredFloat.data() : parentWidget());
            dw->show();
            dw->d_func()->plug(currentGapRect);
        }
#endif
#if QT_CONFIG(toolbar)
        if (QToolBar *tb = qobject_cast<QToolBar*>(widget))
            tb->d_func()->plug(currentGapRect);
#endif

        savedState.clear();
        currentGapPos.clear();
        pluggingWidget = nullptr;
#if QT_CONFIG(dockwidget)
        setCurrentHoveredFloat(nullptr);
#endif
        //applying the state will make sure that the currentGap is updated correctly
        //and all the geometries (especially the one from the central widget) is correct
        layoutState.apply(QWidgetAnimator::AnimationRule::Stop);

#if QT_CONFIG(dockwidget)
#if QT_CONFIG(tabbar)
        if (qobject_cast<QDockWidget*>(widget) != nullptr) {
            // info() might return null if the widget is destroyed while
            // animating but before the animationFinished signal is received.
            if (QDockAreaLayoutInfo *info = dockInfo(widget))
                info->setCurrentTab(widget);
        }
#endif
#endif
    }

    if (!widgetAnimator.animating()) {
        //all animations are finished
#if QT_CONFIG(dockwidget)
        parentWidget()->update(layoutState.dockAreaLayout.separatorRegion());
#if QT_CONFIG(tabbar)
        showTabBars();
#endif // QT_CONFIG(tabbar)
#endif // QT_CONFIG(dockwidget)
    }

    updateGapIndicator();
}

//  from src/widgets/widgets/qtoolbarlayout.cpp, line 394, as _ZN14QToolBarLayout13layoutActionsERK5QSize
inline bool QToolBarLayout::layoutActions(const QSize &size)
{
    if (dirty)
        updateGeomArray();

    QRect rect(0, 0, size.width(), size.height());

    QList<QWidget*> showWidgets, hideWidgets;

    QToolBar *tb = qobject_cast<QToolBar*>(parentWidget());
    if (!tb)
        return false;
    QStyle *style = tb->style();
    QStyleOptionToolBar opt;
    tb->initStyleOption(&opt);
    const int handleExtent = movable()
            ? style->pixelMetric(QStyle::PM_ToolBarHandleExtent, &opt, tb) : 0;
    const QMargins margins = contentsMargins();
    const int spacing = this->spacing();
    const int extensionExtent = style->pixelMetric(QStyle::PM_ToolBarExtensionExtent, &opt, tb);
    Qt::Orientation o = tb->orientation();
    bool extensionMenuContainsOnlyWidgetActions = true;

    int space = pick(o, rect.size()) - pick(o, margins) - handleExtent;
    if (space <= 0)
        return false;  // nothing to do.

    if (popupMenu)
        popupMenu->clear();

    bool ranOutOfSpace = false;
    int rows = 0;
    int rowPos = perp(o, rect.topLeft()) + perp(o, QSize(margins.top(), margins.left()));
    int i = 0;
    while (i < items.size()) {
        QList<QLayoutStruct> a = geomArray;

        int start = i;
        int size = 0;
        int prev = -1;
        int rowHeight = 0;
        int count = 0;
        int maximumSize = 0;
        bool expansiveRow = false;
        for (; i < items.size(); ++i) {
            if (a[i].empty)
                continue;

            int newSize = size + (count == 0 ? 0 : spacing) + a[i].minimumSize;
            if (prev != -1 && newSize > space) {
                if (rows == 0)
                    ranOutOfSpace = true;
                // do we have to move the previous item to the next line to make space for
                // the extension button?
                if (count > 1 && size + spacing + extensionExtent > space)
                    i = prev;
                break;
            }

            if (expanded)
                rowHeight = qMax(rowHeight, perp(o, items.at(i)->sizeHint()));
            expansiveRow = expansiveRow || a[i].expansive;
            size = newSize;
            maximumSize += spacing + (a[i].expansive ? a[i].maximumSize : a[i].smartSizeHint());
            prev = i;
            ++count;
        }

        // stretch at the end
        a[i].sizeHint = 0;
        a[i].maximumSize = QWIDGETSIZE_MAX;
        a[i].minimumSize = 0;
        a[i].expansive = true;
        a[i].stretch = 0;
        a[i].empty = true;

        if (expansiveRow && maximumSize < space) {
            expansiveRow = false;
            a[i].maximumSize = space - maximumSize;
        }

        qGeomCalc(a, start, i - start + (expansiveRow ? 0 : 1), 0,
                    space - (ranOutOfSpace ? (extensionExtent + spacing) : 0),
                    spacing);

        for (int j = start; j < i; ++j) {
            QToolBarItem *item = items.at(j);

            if (a[j].empty) {
                if (!item->widget()->isHidden())
                    hideWidgets << item->widget();
                continue;
            }

            QPoint pos;
            rpick(o, pos) = pick(o, QSize(margins.top(), margins.left())) + handleExtent + a[j].pos;
            rperp(o, pos) = rowPos;
            QSize size;
            rpick(o, size) = a[j].size;
            if (expanded)
                rperp(o, size) = rowHeight;
            else
                rperp(o, size) = perp(o, rect.size()) - perp(o, margins);
            QRect r(pos, size);

            if (o == Qt::Horizontal)
                r = QStyle::visualRect(parentWidget()->layoutDirection(), rect, r);

            item->setGeometry(r);

            if (item->widget()->isHidden())
                showWidgets << item->widget();
        }

        if (!expanded) {
            for (int j = i; j < items.size(); ++j) {
                QToolBarItem *item = items.at(j);
                if (!item->widget()->isHidden())
                    hideWidgets << item->widget();
                if (popupMenu) {
                    if (!defaultWidgetAction(item)) {
                        popupMenu->addAction(item->action);
                        extensionMenuContainsOnlyWidgetActions = false;
                    }
                }
            }
            break;
        }

        rowPos += rowHeight + spacing;
        ++rows;
    }

    // if we are using a popup menu, not the expadning toolbar effect, we cannot move custom
    // widgets into the menu. If only custom widget actions are chopped off, the popup menu
    // is empty. So we show the little extension button to show something is chopped off,
    // but we make it disabled.
    extension->setEnabled(popupMenu == nullptr || !extensionMenuContainsOnlyWidgetActions);

    // we have to do the show/hide here, because it triggers more calls to setGeometry :(
    for (int i = 0; i < showWidgets.size(); ++i)
        showWidgets.at(i)->show();
    for (int i = 0; i < hideWidgets.size(); ++i)
        hideWidgets.at(i)->hide();

    return ranOutOfSpace;
}

//  from src/widgets/widgets/qwidgetanimator.cpp, line 18, as _ZN15QWidgetAnimatorC1EP17QMainWindowLayout
inline QWidgetAnimator::QWidgetAnimator(QMainWindowLayout *layout)
#if QT_CONFIG(mainwindow)
: m_mainWindowLayout(layout)
#endif
{
    Q_UNUSED(layout);
}

//  from src/widgets/widgets/qwidgetanimator.cpp, line 78, as _ZNK15QWidgetAnimator9animatingEv
inline bool QWidgetAnimator::animating() const
{
    auto isActiveAnimation = [](const QPointer<QPropertyAnimation> &p) { return !p.isNull(); };
    return !std::all_of(m_animation_map.begin(), m_animation_map.end(), isActiveAnimation);
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QWidgetAnimator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QWidgetAnimator10metaObjectEv(
    const QWidgetAnimator *self) {
  return self->metaObject();
}

//  void *QWidgetAnimator::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QWidgetAnimator11qt_metacastEPKc(
    QWidgetAnimator *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWidgetAnimator::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QWidgetAnimator11qt_metacallEN11QMetaObject4CallEiPPv(
    QWidgetAnimator *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWidgetAnimator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QWidgetAnimator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWidgetAnimator::tr(s, c, n));
}

//  QWidgetAnimator::QWidgetAnimator(QMainWindowLayout *layout)
extern "C" Q_DECL_EXPORT
QWidgetAnimator *ritual_ZN15QWidgetAnimatorC1EP17QMainWindowLayout(
    QMainWindowLayout *layout) {
  return new QWidgetAnimator(layout);
}

//  bool QWidgetAnimator::animating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QWidgetAnimator9animatingEv(const QWidgetAnimator *self) {
  return self->animating();
}
