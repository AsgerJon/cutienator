//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_dnditem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_dnditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A qdesigner_internal::QDesignerDnDItem that Python can take functions over in. Every qdesigner_internal::QDesignerDnDItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*Cuteqdesigner_internal_QDesignerDnDItemCall0)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerDnDItemCall1)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerDnDItemCall2)(const void *, int *);
typedef const QPoint * (*Cuteqdesigner_internal_QDesignerDnDItemCall3)(const void *, int *);
typedef void * (*Cuteqdesigner_internal_QDesignerDnDItemCall4)(const void *, int *);
typedef int (*Cuteqdesigner_internal_QDesignerDnDItemCall5)(const void *, int *);
class Cuteqdesigner_internal_QDesignerDnDItem : public qdesigner_internal::QDesignerDnDItem {
public:
  using qdesigner_internal::QDesignerDnDItem::QDesignerDnDItem;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface5domUiEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface10decorationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface6widgetEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface7hotSpotEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface6sourceEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface4typeEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  DomUI *qdesigner_internal::QDesignerDnDItem::domUi() const
  DomUI *domUi() const override {
    if (taken[0]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerDnDItemCall0 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerDnDItemCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomUI *>(given);
    }
    return qdesigner_internal::QDesignerDnDItem::domUi();
  }

  //  QWidget *qdesigner_internal::QDesignerDnDItem::decoration() const
  QWidget *decoration() const override {
    if (taken[1]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerDnDItemCall1 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerDnDItemCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::QDesignerDnDItem::decoration();
  }

  //  QWidget *qdesigner_internal::QDesignerDnDItem::widget() const
  QWidget *widget() const override {
    if (taken[2]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerDnDItemCall2 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerDnDItemCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::QDesignerDnDItem::widget();
  }

  //  QPoint qdesigner_internal::QDesignerDnDItem::hotSpot() const
  QPoint hotSpot() const override {
    if (taken[3]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerDnDItemCall3 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerDnDItemCall3>(taken[3]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return qdesigner_internal::QDesignerDnDItem::hotSpot();
  }

  //  QWidget *qdesigner_internal::QDesignerDnDItem::source() const
  QWidget *source() const override {
    if (taken[4]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerDnDItemCall4 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerDnDItemCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return qdesigner_internal::QDesignerDnDItem::source();
  }

  //  DropType qdesigner_internal::QDesignerDnDItem::type() const
  QDesignerDnDItemInterface::DropType type() const override {
    if (taken[5]) {
      int handled = 0;
      Cuteqdesigner_internal_QDesignerDnDItemCall5 call = reinterpret_cast<Cuteqdesigner_internal_QDesignerDnDItemCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerDnDItemInterface::DropType>(given);
    }
    return qdesigner_internal::QDesignerDnDItem::type();
  }
};

//  qdesigner_internal::QDesignerDnDItem::QDesignerDnDItem(DropType type,
//      QWidget *source)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerDnDItem *ritual_ZN18qdesigner_internal16QDesignerDnDItemC1EN25QDesignerDnDItemInterface8DropTypeEP7QWidget(
    QDesignerDnDItemInterface::DropType type,
    QWidget *source) {
  return new Cuteqdesigner_internal_QDesignerDnDItem(type, source);
}

//  qdesigner_internal::QDesignerDnDItem::~QDesignerDnDItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16QDesignerDnDItemD1Ev(
    qdesigner_internal::QDesignerDnDItem *self) {
  delete self;
}

//  DomUI *qdesigner_internal::QDesignerDnDItem::domUi() const
extern "C" Q_DECL_EXPORT
DomUI *ritual_ZNK18qdesigner_internal16QDesignerDnDItem5domUiEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->domUi();
}

//  QWidget *qdesigner_internal::QDesignerDnDItem::decoration() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal16QDesignerDnDItem10decorationEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->decoration();
}

//  QWidget *qdesigner_internal::QDesignerDnDItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal16QDesignerDnDItem6widgetEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->widget();
}

//  QPoint qdesigner_internal::QDesignerDnDItem::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK18qdesigner_internal16QDesignerDnDItem7hotSpotEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return new QPoint(self->hotSpot());
}

//  QWidget *qdesigner_internal::QDesignerDnDItem::source() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK18qdesigner_internal16QDesignerDnDItem6sourceEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->source();
}

//  DropType qdesigner_internal::QDesignerDnDItem::type() const
extern "C" Q_DECL_EXPORT
QDesignerDnDItemInterface::DropType ritual_ZNK18qdesigner_internal16QDesignerDnDItem4typeEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->type();
}

//  void qdesigner_internal::QDesignerDnDItem::setDomUi(DomUI *dom_ui)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16QDesignerDnDItem8setDomUiEP5DomUI(
    qdesigner_internal::QDesignerDnDItem *self,
    DomUI *dom_ui) {
  self->setDomUi(dom_ui);
}

//  void qdesigner_internal::QDesignerDnDItem::init(DomUI *ui, QWidget
//      *widget, QWidget *decoration, const QPoint &global_mouse_pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16QDesignerDnDItem4initEP5DomUIP7QWidgetS4_RK6QPoint(
    qdesigner_internal::QDesignerDnDItem *self,
    DomUI *ui,
    QWidget *widget,
    QWidget *decoration,
    const QPoint *global_mouse_pos) {
  self->init(ui, widget, decoration, *global_mouse_pos);
}

//  a Python function taken by a Cuteqdesigner_internal_QDesignerDnDItem, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_qdesigner_internal_QDesignerDnDItem(
    qdesigner_internal::QDesignerDnDItem *self,
    const char *key,
    void *call) {
  return static_cast<Cuteqdesigner_internal_QDesignerDnDItem *>(self)->take(key, call);
}

//  DomUI *qdesigner_internal::QDesignerDnDItem::domUi() const
extern "C" Q_DECL_EXPORT
DomUI *ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem5domUiEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->qdesigner_internal::QDesignerDnDItem::domUi();
}

//  QWidget *qdesigner_internal::QDesignerDnDItem::decoration() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem10decorationEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->qdesigner_internal::QDesignerDnDItem::decoration();
}

//  QWidget *qdesigner_internal::QDesignerDnDItem::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem6widgetEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->qdesigner_internal::QDesignerDnDItem::widget();
}

//  QPoint qdesigner_internal::QDesignerDnDItem::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem7hotSpotEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return new QPoint(self->qdesigner_internal::QDesignerDnDItem::hotSpot());
}

//  QWidget *qdesigner_internal::QDesignerDnDItem::source() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem6sourceEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->qdesigner_internal::QDesignerDnDItem::source();
}

//  DropType qdesigner_internal::QDesignerDnDItem::type() const
extern "C" Q_DECL_EXPORT
QDesignerDnDItemInterface::DropType ritual_own_ZNK18qdesigner_internal16QDesignerDnDItem4typeEv(
    const qdesigner_internal::QDesignerDnDItem *self) {
  return self->qdesigner_internal::QDesignerDnDItem::type();
}
