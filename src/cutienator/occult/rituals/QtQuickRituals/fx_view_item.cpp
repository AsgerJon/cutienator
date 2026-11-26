//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickitemview_p_p.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/private/qquickitemviewfxitem_p_p.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <QtQml/QQmlInfo>
#include "qplatformdefs.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 24, as _ZN10FxViewItemC1EP10QQuickItemP14QQuickItemViewbP22QQuickItemViewAttached
inline FxViewItem::FxViewItem(QQuickItem *i, QQuickItemView *v, bool own, QQuickItemViewAttached *attached)
    : QQuickItemViewFxItem(i, own, QQuickItemViewPrivate::get(v))
    , view(v)
    , attached(attached)
{
}
//  -----------------------------------------------------------------------

//  A FxViewItem that Python can take functions over in. Every FxViewItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxViewItemCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxViewItemCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxViewItemCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxViewItemCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteFxViewItemCall4)(const void *, qreal, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
class CuteFxViewItem : public FxViewItem {
public:
  using FxViewItem::FxViewItem;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem8positionEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem11endPositionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem4sizeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem11sectionSizeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem8containsEdd")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
    return false;
  }

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::position() const
  qreal position() const override {
    if (taken[0]) {
      int handled = 0;
      CuteFxViewItemCall0 call = reinterpret_cast<CuteFxViewItemCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::endPosition() const
  qreal endPosition() const override {
    if (taken[1]) {
      int handled = 0;
      CuteFxViewItemCall1 call = reinterpret_cast<CuteFxViewItemCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::size() const
  qreal size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteFxViewItemCall2 call = reinterpret_cast<CuteFxViewItemCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::sectionSize() const
  qreal sectionSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteFxViewItemCall3 call = reinterpret_cast<CuteFxViewItemCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewFxItem::contains(qreal x, qreal y) const
  bool contains(qreal x, qreal y) const override {
    if (taken[4]) {
      int handled = 0;
      CuteFxViewItemCall4 call = reinterpret_cast<CuteFxViewItemCall4>(taken[4]);
      bool given = call(this, x, y, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)
};

//  FxViewItem::FxViewItem(QQuickItem *a0, QQuickItemView *a1, bool own,
//      QQuickItemViewAttached *attached)
extern "C" Q_DECL_EXPORT
FxViewItem *ritual_ZN10FxViewItemC1EP10QQuickItemP14QQuickItemViewbP22QQuickItemViewAttached(
    QQuickItem *a0,
    QQuickItemView *a1,
    bool own,
    QQuickItemViewAttached *attached) {
  return new CuteFxViewItem(a0, a1, own, attached);
}

//  a Python function taken by a CuteFxViewItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_FxViewItem(FxViewItem *self, const char *key, void *call) {
  return static_cast<CuteFxViewItem *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_itemview)
#endif  // QT_CONFIG(quick_itemview)
