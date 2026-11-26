//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicslayoutstyleinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicslayoutstyleinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicslayoutstyleinfo_p.h>
#include <QtWidgets/private/qgraphicslayout_p.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qapplication.h>
#include <QtCore/qglobal.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicslayoutitem.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtCore/QtDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 53, as _ZNK24QGraphicsLayoutStyleInfo12windowMarginEN2Qt11OrientationE
inline qreal QGraphicsLayoutStyleInfo::windowMargin(Qt::Orientation orientation) const
{
    return style()->pixelMetric(orientation == Qt::Vertical
                                ? QStyle::PM_LayoutBottomMargin
                                : QStyle::PM_LayoutRightMargin,
                                const_cast<QStyleOption*>(&m_styleOption), widget());
}

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 36, as _ZNK24QGraphicsLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE
inline qreal QGraphicsLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType control1,
                                               QLayoutPolicy::ControlType control2,
                                               Qt::Orientation orientation) const
{
    Q_ASSERT(style());
    return style()->layoutSpacing(QSizePolicy::ControlType(control1), QSizePolicy::ControlType(control2),
                                  orientation, const_cast<QStyleOption*>(&m_styleOption), widget());
}

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 27, as _ZNK24QGraphicsLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE
inline qreal QGraphicsLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::ControlTypes controls1,
                                                      QLayoutPolicy::ControlTypes controls2,
                                                      Qt::Orientation orientation) const
{
    Q_ASSERT(style());
    return style()->combinedLayoutSpacing(QSizePolicy::ControlTypes(int(controls1)), QSizePolicy::ControlTypes(int(controls2)),
                                          orientation, const_cast<QStyleOption*>(&m_styleOption), widget());
}

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 45, as _ZNK24QGraphicsLayoutStyleInfo7spacingEN2Qt11OrientationE
inline qreal QGraphicsLayoutStyleInfo::spacing(Qt::Orientation orientation) const
{
    Q_ASSERT(style());
    return style()->pixelMetric(orientation == Qt::Horizontal
        ? QStyle::PM_LayoutHorizontalSpacing : QStyle::PM_LayoutVerticalSpacing,
        &m_styleOption, widget());
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 175, as _ZNK26QGraphicsLayoutItemPrivate10parentItemEv
inline QGraphicsItem *QGraphicsLayoutItemPrivate::parentItem() const
{
    Q_Q(const QGraphicsLayoutItem);

    const QGraphicsLayoutItem *parent = q;
    while (parent && parent->isLayout()) {
        parent = parent->parentLayoutItem();
    }
    return parent ? parent->graphicsItem() : nullptr;
}

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 15, as _ZN24QGraphicsLayoutStyleInfoC1EPK22QGraphicsLayoutPrivate
inline QGraphicsLayoutStyleInfo::QGraphicsLayoutStyleInfo(const QGraphicsLayoutPrivate *layout)
    : m_layout(layout), m_style(nullptr)
{
    m_widget.reset(new QWidget); // pixelMetric might need a widget ptr
    m_styleOption.initFrom(m_widget.get());
    m_isWindow = m_styleOption.state & QStyle::State_Window;
}

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 23, as _ZN24QGraphicsLayoutStyleInfoD1Ev
inline QGraphicsLayoutStyleInfo::~QGraphicsLayoutStyleInfo()
{
}

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 61, as _ZNK24QGraphicsLayoutStyleInfo6widgetEv
inline QWidget *QGraphicsLayoutStyleInfo::widget() const { return m_widget.get(); }

//  from src/widgets/graphicsview/qgraphicslayoutstyleinfo.cpp, line 63, as _ZNK24QGraphicsLayoutStyleInfo5styleEv
inline QStyle *QGraphicsLayoutStyleInfo::style() const
{
    if (!m_style) {
        Q_ASSERT(m_layout);
        QGraphicsItem *item = m_layout->parentItem();
        m_style = (item && item->isWidget()) ? static_cast<QGraphicsWidget*>(item)->style() : QApplication::style();
    }
    return m_style;
}
//  -----------------------------------------------------------------------

//  A QGraphicsLayoutStyleInfo that Python can take functions over in. Every QGraphicsLayoutStyleInfo
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsLayoutStyleInfoCall0)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsLayoutStyleInfoCall1)(const void *, int, int, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsLayoutStyleInfoCall2)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsLayoutStyleInfoCall3)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsLayoutStyleInfoCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsLayoutStyleInfoCall5)(const void *, int *);
class CuteQGraphicsLayoutStyleInfo : public QGraphicsLayoutStyleInfo {
public:
  using QGraphicsLayoutStyleInfo::QGraphicsLayoutStyleInfo;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo7spacingEN2Qt11OrientationE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo12windowMarginEN2Qt11OrientationE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN24QAbstractLayoutStyleInfo10invalidateEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK24QAbstractLayoutStyleInfo14hasChangedCoreEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::
  //      ControlTypes controls1, QLayoutPolicy::ControlTypes controls2,
  //      Qt::Orientation orientation) const
  qreal combinedLayoutSpacing(
      QLayoutPolicy::ControlTypes controls1,
      QLayoutPolicy::ControlTypes controls2,
      Qt::Orientation orientation) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsLayoutStyleInfoCall0 call = reinterpret_cast<CuteQGraphicsLayoutStyleInfoCall0>(taken[0]);
      qreal given = call(this, static_cast<int>(controls1.toInt()), static_cast<int>(controls2.toInt()), static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutStyleInfo::combinedLayoutSpacing(controls1, controls2, orientation);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal
  //      QGraphicsLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlTy
  //      pe control1, QLayoutPolicy::ControlType control2, Qt::Orientation
  //      orientation) const
  qreal perItemSpacing(
      QLayoutPolicy::ControlType control1,
      QLayoutPolicy::ControlType control2,
      Qt::Orientation orientation) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsLayoutStyleInfoCall1 call = reinterpret_cast<CuteQGraphicsLayoutStyleInfoCall1>(taken[1]);
      qreal given = call(this, static_cast<int>(control1), static_cast<int>(control2), static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutStyleInfo::perItemSpacing(control1, control2, orientation);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsLayoutStyleInfo::spacing(Qt::Orientation orientation)
  //      const
  qreal spacing(Qt::Orientation orientation) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsLayoutStyleInfoCall2 call = reinterpret_cast<CuteQGraphicsLayoutStyleInfoCall2>(taken[2]);
      qreal given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutStyleInfo::spacing(orientation);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsLayoutStyleInfo::windowMargin(Qt::Orientation
  //      orientation) const
  qreal windowMargin(Qt::Orientation orientation) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsLayoutStyleInfoCall3 call = reinterpret_cast<CuteQGraphicsLayoutStyleInfoCall3>(taken[3]);
      qreal given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QGraphicsLayoutStyleInfo::windowMargin(orientation);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsLayoutStyleInfo::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsLayoutStyleInfoCall4 call = reinterpret_cast<CuteQGraphicsLayoutStyleInfoCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsLayoutStyleInfo::invalidate();
  }
#endif  // QT_CONFIG(graphicsview)

  //  bool QAbstractLayoutStyleInfo::hasChangedCore() const
  bool hasChangedCore() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsLayoutStyleInfoCall5 call = reinterpret_cast<CuteQGraphicsLayoutStyleInfoCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractLayoutStyleInfo::hasChangedCore();
  }
};

//  QGraphicsLayoutStyleInfo::QGraphicsLayoutStyleInfo(const
//      QGraphicsLayoutPrivate *layout)
extern "C" Q_DECL_EXPORT
QGraphicsLayoutStyleInfo *ritual_ZN24QGraphicsLayoutStyleInfoC1EPK22QGraphicsLayoutPrivate(
    const QGraphicsLayoutPrivate *layout) {
  return new CuteQGraphicsLayoutStyleInfo(layout);
}

//  QGraphicsLayoutStyleInfo::~QGraphicsLayoutStyleInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsLayoutStyleInfoD1Ev(
    QGraphicsLayoutStyleInfo *self) {
  delete self;
}

//  qreal QGraphicsLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::Cont
//      rolTypes controls1, QLayoutPolicy::ControlTypes controls2,
//      Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QGraphicsLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    int controls1,
    int controls2,
    Qt::Orientation orientation) {
  return self->combinedLayoutSpacing(
      QFlags<QLayoutPolicy::ControlType>::fromInt(controls1),
      QFlags<QLayoutPolicy::ControlType>::fromInt(controls2),
      orientation);
}

//  qreal QGraphicsLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType
//      control1, QLayoutPolicy::ControlType control2, Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QGraphicsLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    QLayoutPolicy::ControlType control1,
    QLayoutPolicy::ControlType control2,
    Qt::Orientation orientation) {
  return self->perItemSpacing(control1, control2, orientation);
}

//  qreal QGraphicsLayoutStyleInfo::spacing(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QGraphicsLayoutStyleInfo7spacingEN2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->spacing(orientation);
}

//  qreal QGraphicsLayoutStyleInfo::windowMargin(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QGraphicsLayoutStyleInfo12windowMarginEN2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->windowMargin(orientation);
}

//  void QGraphicsLayoutStyleInfo::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsLayoutStyleInfo10invalidateEv(
    QGraphicsLayoutStyleInfo *self) {
  self->invalidate();
}

//  QWidget *QGraphicsLayoutStyleInfo::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK24QGraphicsLayoutStyleInfo6widgetEv(
    const QGraphicsLayoutStyleInfo *self) {
  return self->widget();
}

//  QStyle *QGraphicsLayoutStyleInfo::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK24QGraphicsLayoutStyleInfo5styleEv(
    const QGraphicsLayoutStyleInfo *self) {
  return self->style();
}

//  a Python function taken by a CuteQGraphicsLayoutStyleInfo, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsLayoutStyleInfo(
    QGraphicsLayoutStyleInfo *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsLayoutStyleInfo *>(self)->take(key, call);
}

//  qreal QGraphicsLayoutStyleInfo::combinedLayoutSpacing(QLayoutPolicy::Cont
//      rolTypes controls1, QLayoutPolicy::ControlTypes controls2,
//      Qt::Orientation orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QGraphicsLayoutStyleInfo21combinedLayoutSpacingE6QFlagsIN13QLayoutPolicy11ControlTypeEES3_N2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    int controls1,
    int controls2,
    Qt::Orientation orientation) {
  return self->QGraphicsLayoutStyleInfo::combinedLayoutSpacing(
      QFlags<QLayoutPolicy::ControlType>::fromInt(controls1),
      QFlags<QLayoutPolicy::ControlType>::fromInt(controls2),
      orientation);
}

//  qreal QGraphicsLayoutStyleInfo::perItemSpacing(QLayoutPolicy::ControlType
//      control1, QLayoutPolicy::ControlType control2, Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QGraphicsLayoutStyleInfo14perItemSpacingEN13QLayoutPolicy11ControlTypeES1_N2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    QLayoutPolicy::ControlType control1,
    QLayoutPolicy::ControlType control2,
    Qt::Orientation orientation) {
  return self->QGraphicsLayoutStyleInfo::perItemSpacing(
      control1,
      control2,
      orientation);
}

//  qreal QGraphicsLayoutStyleInfo::spacing(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QGraphicsLayoutStyleInfo7spacingEN2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->QGraphicsLayoutStyleInfo::spacing(orientation);
}

//  qreal QGraphicsLayoutStyleInfo::windowMargin(Qt::Orientation orientation)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK24QGraphicsLayoutStyleInfo12windowMarginEN2Qt11OrientationE(
    const QGraphicsLayoutStyleInfo *self,
    Qt::Orientation orientation) {
  return self->QGraphicsLayoutStyleInfo::windowMargin(orientation);
}

//  void QGraphicsLayoutStyleInfo::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QGraphicsLayoutStyleInfo10invalidateEv(
    QGraphicsLayoutStyleInfo *self) {
  self->QGraphicsLayoutStyleInfo::invalidate();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
