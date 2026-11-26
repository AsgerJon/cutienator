//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickstackview_p.h>
#include <QtQuickTemplates2/private/qquickstackview_p_p.h>
#include <QtQuickTemplates2/private/qquickstackelement_p_p.h>
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuickTemplates2/private/qquickstacktransition_p_p.h>
#endif
#include <QtCore/qscopedvaluerollback.h>
#include <QtQml/qjsvalue.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qqmlengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickstackview.cpp, line 1707, as _ZN30QQuickStackViewAttachedPrivate17itemParentChangedEP10QQuickItemS1_
inline void QQuickStackViewAttachedPrivate::itemParentChanged(QQuickItem *item, QQuickItem *parent)
{
    Q_Q(QQuickStackViewAttached);
    int oldIndex = element ? element->index : -1;
    QQuickStackView *oldView = element ? element->view : nullptr;
    QQuickStackView::Status oldStatus = element ? element->status : QQuickStackView::Inactive;

    QQuickStackView *newView = qobject_cast<QQuickStackView *>(parent);
    element = newView ? QQuickStackViewPrivate::get(newView)->findElement(item) : nullptr;

    int newIndex = element ? element->index : -1;
    QQuickStackView::Status newStatus = element ? element->status : QQuickStackView::Inactive;

    if (oldIndex != newIndex)
        emit q->indexChanged();
    if (oldView != newView)
        emit q->viewChanged();
    if (oldStatus != newStatus)
        emit q->statusChanged();
}
//  -----------------------------------------------------------------------

//  A QQuickStackViewAttachedPrivate that Python can take functions over in. Every QQuickStackViewAttachedPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickStackViewAttachedPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
class CuteQQuickStackViewAttachedPrivate : public QQuickStackViewAttachedPrivate {
public:
  using QQuickStackViewAttachedPrivate::QQuickStackViewAttachedPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QQuickStackViewAttachedPrivate17itemParentChangedEP10QQuickItemS1_")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuickStackViewAttachedPrivate::itemParentChanged(QQuickItem
  //      *item, QQuickItem *parent)
  void itemParentChanged(QQuickItem *item, QQuickItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStackViewAttachedPrivateCall0 call = reinterpret_cast<CuteQQuickStackViewAttachedPrivateCall0>(taken[0]);
      call(this, item, parent, &handled);
      if (handled) return;
    }
    QQuickStackViewAttachedPrivate::itemParentChanged(item, parent);
  }
};

//  QQuickStackViewAttached *QQuickStackViewAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickStackViewAttached *ritual_ZN30QQuickStackViewAttachedPrivate6q_funcEv(
    QQuickStackViewAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickStackViewAttached *QQuickStackViewAttachedPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickStackViewAttached *ritual_ZNK30QQuickStackViewAttachedPrivate6q_funcEv(
    const QQuickStackViewAttachedPrivate *self) {
  return self->q_func();
}

//  QQuickStackViewAttachedPrivate
//      *QQuickStackViewAttachedPrivate::get(QQuickStackViewAttached
//      *attached)
extern "C" Q_DECL_EXPORT
QQuickStackViewAttachedPrivate *ritual_ZN30QQuickStackViewAttachedPrivate3getEP23QQuickStackViewAttached(
    QQuickStackViewAttached *attached) {
  return QQuickStackViewAttachedPrivate::get(attached);
}

//  void QQuickStackViewAttachedPrivate::itemParentChanged(QQuickItem *item,
//      QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickStackViewAttachedPrivate17itemParentChangedEP10QQuickItemS1_(
    QQuickStackViewAttachedPrivate *self,
    QQuickItem *item,
    QQuickItem *parent) {
  self->itemParentChanged(item, parent);
}

//  a Python function taken by a CuteQQuickStackViewAttachedPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStackViewAttachedPrivate(
    QQuickStackViewAttachedPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStackViewAttachedPrivate *>(self)->take(key, call);
}
