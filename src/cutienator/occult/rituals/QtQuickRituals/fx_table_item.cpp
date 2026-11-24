//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktableview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A FxTableItem that Python can take functions over in. Every FxTableItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxTableItemCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxTableItemCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxTableItemCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteFxTableItemCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteFxTableItemCall4)(const void *, qreal, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
class CuteFxTableItem : public FxTableItem {
public:
  using FxTableItem::FxTableItem;
  CuteFxTableItem(const FxTableItem &other) : FxTableItem(other) {}
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
  //  qreal FxTableItem::position() const
  qreal position() const override {
    if (taken[0]) {
      int handled = 0;
      CuteFxTableItemCall0 call = reinterpret_cast<CuteFxTableItemCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return FxTableItem::position();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal FxTableItem::endPosition() const
  qreal endPosition() const override {
    if (taken[1]) {
      int handled = 0;
      CuteFxTableItemCall1 call = reinterpret_cast<CuteFxTableItemCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return FxTableItem::endPosition();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal FxTableItem::size() const
  qreal size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteFxTableItemCall2 call = reinterpret_cast<CuteFxTableItemCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return FxTableItem::size();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal FxTableItem::sectionSize() const
  qreal sectionSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteFxTableItemCall3 call = reinterpret_cast<CuteFxTableItemCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return FxTableItem::sectionSize();
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool FxTableItem::contains(qreal a0, qreal a1) const
  bool contains(qreal a0, qreal a1) const override {
    if (taken[4]) {
      int handled = 0;
      CuteFxTableItemCall4 call = reinterpret_cast<CuteFxTableItemCall4>(taken[4]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return FxTableItem::contains(a0, a1);
  }
#endif  // QT_CONFIG(quick_itemview)
};

//  FxTableItem::FxTableItem(QQuickItem *item, QQuickTableView *table, bool
//      own)
extern "C" Q_DECL_EXPORT
FxTableItem *ritual_ZN11FxTableItemC1EP10QQuickItemP15QQuickTableViewb(
    QQuickItem *item,
    QQuickTableView *table,
    bool own) {
  return new CuteFxTableItem(item, table, own);
}

//  qreal FxTableItem::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11FxTableItem8positionEv(const FxTableItem *self) {
  return self->position();
}

//  qreal FxTableItem::endPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11FxTableItem11endPositionEv(const FxTableItem *self) {
  return self->endPosition();
}

//  qreal FxTableItem::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11FxTableItem4sizeEv(const FxTableItem *self) {
  return self->size();
}

//  qreal FxTableItem::sectionSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK11FxTableItem11sectionSizeEv(const FxTableItem *self) {
  return self->sectionSize();
}

//  bool FxTableItem::contains(qreal a0, qreal a1) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11FxTableItem8containsEdd(
    const FxTableItem *self,
    qreal a0,
    qreal a1) {
  return self->contains(a0, a1);
}

//  FxTableItem::~FxTableItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN11FxTableItemD1Ev(FxTableItem *self) {
  delete self;
}

//  a Python function taken by a CuteFxTableItem, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_FxTableItem(
    FxTableItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteFxTableItem *>(self)->take(key, call);
}

//  qreal FxTableItem::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK11FxTableItem8positionEv(const FxTableItem *self) {
  return self->FxTableItem::position();
}

//  qreal FxTableItem::endPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK11FxTableItem11endPositionEv(const FxTableItem *self) {
  return self->FxTableItem::endPosition();
}

//  qreal FxTableItem::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK11FxTableItem4sizeEv(const FxTableItem *self) {
  return self->FxTableItem::size();
}

//  qreal FxTableItem::sectionSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK11FxTableItem11sectionSizeEv(const FxTableItem *self) {
  return self->FxTableItem::sectionSize();
}

//  bool FxTableItem::contains(qreal a0, qreal a1) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11FxTableItem8containsEdd(
    const FxTableItem *self,
    qreal a0,
    qreal a1) {
  return self->FxTableItem::contains(a0, a1);
}

#endif  // QT_CONFIG(quick_tableview)
