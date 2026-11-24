//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsgridlayoutengine_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsgridlayoutengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qgraphicsgridlayoutengine_p.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/private/qgraphicslayout_p.h>
#include <QtWidgets/qgraphicswidget.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 17, as _ZNK29QGraphicsGridLayoutEngineItem20hasDynamicConstraintEv
inline bool QGraphicsGridLayoutEngineItem::hasDynamicConstraint() const
{
    return QGraphicsLayoutItemPrivate::get(q_layoutItem)->hasHeightForWidth()
        || QGraphicsLayoutItemPrivate::get(q_layoutItem)->hasWidthForHeight();
}

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 23, as _ZNK29QGraphicsGridLayoutEngineItem28dynamicConstraintOrientationEv
inline Qt::Orientation QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation() const
{
    if (QGraphicsLayoutItemPrivate::get(q_layoutItem)->hasHeightForWidth())
        return Qt::Vertical;
    else //if (QGraphicsLayoutItemPrivate::get(q_layoutItem)->hasWidthForHeight())
        return Qt::Horizontal;
}

//  from src/widgets/graphicsview/qgraphicsgridlayoutengine.cpp, line 37, as _ZNK29QGraphicsGridLayoutEngineItem7isEmptyEv
inline bool QGraphicsGridLayoutEngineItem::isEmpty() const
{
    return q_layoutItem->isEmpty();
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 239, as _ZNK26QGraphicsLayoutItemPrivate17hasHeightForWidthEv
inline bool QGraphicsLayoutItemPrivate::hasHeightForWidth() const
{
    Q_Q(const QGraphicsLayoutItem);
    if (isLayout) {
        const QGraphicsLayout *l = static_cast<const QGraphicsLayout *>(q);
        for (int i = l->count() - 1; i >= 0; --i) {
            if (QGraphicsLayoutItemPrivate::get(l->itemAt(i))->hasHeightForWidth())
                return true;
        }
    } else if (QGraphicsItem *item = q->graphicsItem()) {
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (w->layout()) {
                return QGraphicsLayoutItemPrivate::get(w->layout())->hasHeightForWidth();
            }
        }
    }
    return q->sizePolicy().hasHeightForWidth();
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 259, as _ZNK26QGraphicsLayoutItemPrivate17hasWidthForHeightEv
inline bool QGraphicsLayoutItemPrivate::hasWidthForHeight() const
{
    Q_Q(const QGraphicsLayoutItem);
    if (isLayout) {
        const QGraphicsLayout *l = static_cast<const QGraphicsLayout *>(q);
        for (int i = l->count() - 1; i >= 0; --i) {
            if (QGraphicsLayoutItemPrivate::get(l->itemAt(i))->hasWidthForHeight())
                return true;
        }
    } else if (QGraphicsItem *item = q->graphicsItem()) {
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (w->layout()) {
                return QGraphicsLayoutItemPrivate::get(w->layout())->hasWidthForHeight();
            }
        }
    }
    return q->sizePolicy().hasWidthForHeight();
}
//  -----------------------------------------------------------------------

//  A QGraphicsGridLayoutEngineItem that Python can take functions over in. Every QGraphicsGridLayoutEngineItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsGridLayoutEngineItemCall0)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsGridLayoutEngineItemCall1)(const void *, int, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef const QSizeF * (*CuteQGraphicsGridLayoutEngineItemCall2)(const void *, int, const QSizeF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsGridLayoutEngineItemCall3)(const void *, const QRectF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsGridLayoutEngineItemCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef int (*CuteQGraphicsGridLayoutEngineItemCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsGridLayoutEngineItemCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
typedef QString * (*CuteQGraphicsGridLayoutEngineItemCall7)(const void *, int *);
class CuteQGraphicsGridLayoutEngineItem : public QGraphicsGridLayoutEngineItem {
public:
  using QGraphicsGridLayoutEngineItem::QGraphicsGridLayoutEngineItem;
  CuteQGraphicsGridLayoutEngineItem(const QGraphicsGridLayoutEngineItem &other) : QGraphicsGridLayoutEngineItem(other) {}
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem10sizePolicyEN2Qt11OrientationE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem12controlTypesE10LayoutSide")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem8sizeHintEN2Qt8SizeHintERK6QSizeF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN15QGridLayoutItem11setGeometryERK6QRectF")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem20hasDynamicConstraintEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem28dynamicConstraintOrientationEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem7isEmptyEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK15QGridLayoutItem8toStringEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  QLayoutPolicy::Policy
  //      QGraphicsGridLayoutEngineItem::sizePolicy(Qt::Orientation
  //      orientation) const
  QLayoutPolicy::Policy sizePolicy(
      Qt::Orientation orientation) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall0 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall0>(taken[0]);
      int given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return QFlags<QLayoutPolicy::PolicyFlag>::fromInt(given);
    }
    return QGraphicsGridLayoutEngineItem::sizePolicy(orientation);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QLayoutPolicy::ControlTypes
  //      QGraphicsGridLayoutEngineItem::controlTypes(LayoutSide a0) const
  QLayoutPolicy::ControlTypes controlTypes(LayoutSide a0) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall1 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall1>(taken[1]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return QFlags<QLayoutPolicy::ControlType>::fromInt(given);
    }
    return QGraphicsGridLayoutEngineItem::controlTypes(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  QSizeF QGraphicsGridLayoutEngineItem::sizeHint(Qt::SizeHint which,
  //      const QSizeF &constraint) const
  QSizeF sizeHint(
      Qt::SizeHint which,
      const QSizeF &constraint) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall2 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall2>(taken[2]);
      const QSizeF * given = call(this, static_cast<int>(which), &constraint, &handled);
      if (handled && given) return *given;
    }
    return QGraphicsGridLayoutEngineItem::sizeHint(which, constraint);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsGridLayoutEngineItem::setGeometry(const QRectF &rect)
  void setGeometry(const QRectF &rect) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall3 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall3>(taken[3]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QGraphicsGridLayoutEngineItem::setGeometry(rect);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsGridLayoutEngineItem::hasDynamicConstraint() const
  bool hasDynamicConstraint() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall4 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsGridLayoutEngineItem::hasDynamicConstraint();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  Qt::Orientation
  //      QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation()
  //      const
  Qt::Orientation dynamicConstraintOrientation() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall5 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt::Orientation>(given);
    }
    return QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsGridLayoutEngineItem::isEmpty() const
  bool isEmpty() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall6 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsGridLayoutEngineItem::isEmpty();
  }
#endif  // QT_CONFIG(graphicsview)

  //  QString QGridLayoutItem::toString() const
  QString toString() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsGridLayoutEngineItemCall7 call = reinterpret_cast<CuteQGraphicsGridLayoutEngineItemCall7>(taken[7]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGridLayoutItem::toString();
  }
};

//  QLayoutPolicy::Policy
//      QGraphicsGridLayoutEngineItem::sizePolicy(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QGraphicsGridLayoutEngineItem10sizePolicyEN2Qt11OrientationE(
    const QGraphicsGridLayoutEngineItem *self,
    Qt::Orientation orientation) {
  return static_cast<int>(self->sizePolicy(orientation).toInt());
}

//  QLayoutPolicy::ControlTypes
//      QGraphicsGridLayoutEngineItem::controlTypes(LayoutSide a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QGraphicsGridLayoutEngineItem12controlTypesE10LayoutSide(
    const QGraphicsGridLayoutEngineItem *self,
    LayoutSide a0) {
  return static_cast<int>(self->controlTypes(a0).toInt());
}

//  QSizeF QGraphicsGridLayoutEngineItem::sizeHint(Qt::SizeHint which, const
//      QSizeF &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK29QGraphicsGridLayoutEngineItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsGridLayoutEngineItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(self->sizeHint(which, *constraint));
}

//  void QGraphicsGridLayoutEngineItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGraphicsGridLayoutEngineItem11setGeometryERK6QRectF(
    QGraphicsGridLayoutEngineItem *self,
    const QRectF *rect) {
  self->setGeometry(*rect);
}

//  bool QGraphicsGridLayoutEngineItem::hasDynamicConstraint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QGraphicsGridLayoutEngineItem20hasDynamicConstraintEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->hasDynamicConstraint();
}

//  Qt::Orientation
//      QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK29QGraphicsGridLayoutEngineItem28dynamicConstraintOrientationEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->dynamicConstraintOrientation();
}

//  bool QGraphicsGridLayoutEngineItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QGraphicsGridLayoutEngineItem7isEmptyEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->isEmpty();
}

//  QGraphicsLayoutItem *QGraphicsGridLayoutEngineItem::layoutItem() const
extern "C" Q_DECL_EXPORT
QGraphicsLayoutItem *ritual_ZNK29QGraphicsGridLayoutEngineItem10layoutItemEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->layoutItem();
}

//  QGraphicsGridLayoutEngineItem::~QGraphicsGridLayoutEngineItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGraphicsGridLayoutEngineItemD1Ev(
    QGraphicsGridLayoutEngineItem *self) {
  delete self;
}

//  a Python function taken by a CuteQGraphicsGridLayoutEngineItem, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsGridLayoutEngineItem(
    QGraphicsGridLayoutEngineItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsGridLayoutEngineItem *>(self)->take(key, call);
}

//  QLayoutPolicy::Policy
//      QGraphicsGridLayoutEngineItem::sizePolicy(Qt::Orientation
//      orientation) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QGraphicsGridLayoutEngineItem10sizePolicyEN2Qt11OrientationE(
    const QGraphicsGridLayoutEngineItem *self,
    Qt::Orientation orientation) {
  return static_cast<int>(
      self->QGraphicsGridLayoutEngineItem::sizePolicy(
          orientation).toInt());
}

//  QLayoutPolicy::ControlTypes
//      QGraphicsGridLayoutEngineItem::controlTypes(LayoutSide a0) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QGraphicsGridLayoutEngineItem12controlTypesE10LayoutSide(
    const QGraphicsGridLayoutEngineItem *self,
    LayoutSide a0) {
  return static_cast<int>(
      self->QGraphicsGridLayoutEngineItem::controlTypes(
          a0).toInt());
}

//  QSizeF QGraphicsGridLayoutEngineItem::sizeHint(Qt::SizeHint which, const
//      QSizeF &constraint) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_own_ZNK29QGraphicsGridLayoutEngineItem8sizeHintEN2Qt8SizeHintERK6QSizeF(
    const QGraphicsGridLayoutEngineItem *self,
    Qt::SizeHint which,
    const QSizeF *constraint) {
  return new QSizeF(
      self->QGraphicsGridLayoutEngineItem::sizeHint(
          which,
          *constraint));
}

//  void QGraphicsGridLayoutEngineItem::setGeometry(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QGraphicsGridLayoutEngineItem11setGeometryERK6QRectF(
    QGraphicsGridLayoutEngineItem *self,
    const QRectF *rect) {
  self->QGraphicsGridLayoutEngineItem::setGeometry(*rect);
}

//  bool QGraphicsGridLayoutEngineItem::hasDynamicConstraint() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QGraphicsGridLayoutEngineItem20hasDynamicConstraintEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->QGraphicsGridLayoutEngineItem::hasDynamicConstraint();
}

//  Qt::Orientation
//      QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_own_ZNK29QGraphicsGridLayoutEngineItem28dynamicConstraintOrientationEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->QGraphicsGridLayoutEngineItem::dynamicConstraintOrientation();
}

//  bool QGraphicsGridLayoutEngineItem::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK29QGraphicsGridLayoutEngineItem7isEmptyEv(
    const QGraphicsGridLayoutEngineItem *self) {
  return self->QGraphicsGridLayoutEngineItem::isEmpty();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
