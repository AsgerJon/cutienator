//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/abstractdnditem.h, Qt 6.12.0. Changes made here are lost.
#include <QtDesigner/abstractdnditem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDesignerDnDItemInterface that Python can take functions over in. Every QDesignerDnDItemInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQDesignerDnDItemInterfaceCall0)(const void *, int *);
typedef void * (*CuteQDesignerDnDItemInterfaceCall1)(const void *, int *);
typedef void * (*CuteQDesignerDnDItemInterfaceCall2)(const void *, int *);
typedef const QPoint * (*CuteQDesignerDnDItemInterfaceCall3)(const void *, int *);
typedef int (*CuteQDesignerDnDItemInterfaceCall4)(const void *, int *);
typedef void * (*CuteQDesignerDnDItemInterfaceCall5)(const void *, int *);
class CuteQDesignerDnDItemInterface : public QDesignerDnDItemInterface {
public:
  using QDesignerDnDItemInterface::QDesignerDnDItemInterface;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface5domUiEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface6widgetEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface10decorationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface7hotSpotEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface4typeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QDesignerDnDItemInterface6sourceEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  DomUI *QDesignerDnDItemInterface::domUi() const
  DomUI *domUi() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesignerDnDItemInterfaceCall0 call = reinterpret_cast<CuteQDesignerDnDItemInterfaceCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DomUI *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerDnDItemInterface::widget() const
  QWidget *widget() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesignerDnDItemInterfaceCall1 call = reinterpret_cast<CuteQDesignerDnDItemInterfaceCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QWidget *QDesignerDnDItemInterface::decoration() const
  QWidget *decoration() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesignerDnDItemInterfaceCall2 call = reinterpret_cast<CuteQDesignerDnDItemInterfaceCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }

  //  QPoint QDesignerDnDItemInterface::hotSpot() const
  QPoint hotSpot() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesignerDnDItemInterfaceCall3 call = reinterpret_cast<CuteQDesignerDnDItemInterfaceCall3>(taken[3]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  DropType QDesignerDnDItemInterface::type() const
  QDesignerDnDItemInterface::DropType type() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesignerDnDItemInterfaceCall4 call = reinterpret_cast<CuteQDesignerDnDItemInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDesignerDnDItemInterface::DropType>(given);
    }
    return {};
  }

  //  QWidget *QDesignerDnDItemInterface::source() const
  QWidget *source() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesignerDnDItemInterfaceCall5 call = reinterpret_cast<CuteQDesignerDnDItemInterfaceCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWidget *>(given);
    }
    return {};
  }
};

//  QDesignerDnDItemInterface::~QDesignerDnDItemInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QDesignerDnDItemInterfaceD1Ev(
    QDesignerDnDItemInterface *self) {
  delete self;
}

//  DomUI *QDesignerDnDItemInterface::domUi() const
extern "C" Q_DECL_EXPORT
DomUI *ritual_ZNK25QDesignerDnDItemInterface5domUiEv(
    const QDesignerDnDItemInterface *self) {
  return self->domUi();
}

//  QWidget *QDesignerDnDItemInterface::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK25QDesignerDnDItemInterface6widgetEv(
    const QDesignerDnDItemInterface *self) {
  return self->widget();
}

//  QWidget *QDesignerDnDItemInterface::decoration() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK25QDesignerDnDItemInterface10decorationEv(
    const QDesignerDnDItemInterface *self) {
  return self->decoration();
}

//  QPoint QDesignerDnDItemInterface::hotSpot() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK25QDesignerDnDItemInterface7hotSpotEv(
    const QDesignerDnDItemInterface *self) {
  return new QPoint(self->hotSpot());
}

//  DropType QDesignerDnDItemInterface::type() const
extern "C" Q_DECL_EXPORT
QDesignerDnDItemInterface::DropType ritual_ZNK25QDesignerDnDItemInterface4typeEv(
    const QDesignerDnDItemInterface *self) {
  return self->type();
}

//  QWidget *QDesignerDnDItemInterface::source() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK25QDesignerDnDItemInterface6sourceEv(
    const QDesignerDnDItemInterface *self) {
  return self->source();
}

//  a Python function taken by a CuteQDesignerDnDItemInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesignerDnDItemInterface(
    QDesignerDnDItemInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesignerDnDItemInterface *>(self)->take(key, call);
}

//  QList<QDesignerDnDItemInterface *>::QList()
extern "C" Q_DECL_EXPORT
QList<QDesignerDnDItemInterface *> *ritual_list_make_QDesignerDnDItemInterface_ptr() {
  return new QList<QDesignerDnDItemInterface *>();
}

//  void QList<QDesignerDnDItemInterface *>::append(const
//      QDesignerDnDItemInterface * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDesignerDnDItemInterface_ptr(
    QList<QDesignerDnDItemInterface *> *self,
    QDesignerDnDItemInterface *element) {
  self->append(element);
}

//  qsizetype QList<QDesignerDnDItemInterface *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDesignerDnDItemInterface_ptr(
    const QList<QDesignerDnDItemInterface *> *self) {
  return self->size();
}

//  const QDesignerDnDItemInterface * &QList<QDesignerDnDItemInterface
//      *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDesignerDnDItemInterface *ritual_list_at_QDesignerDnDItemInterface_ptr(
    const QList<QDesignerDnDItemInterface *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QDesignerDnDItemInterface *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDesignerDnDItemInterface_ptr(
    QList<QDesignerDnDItemInterface *> *self) {
  delete self;
}
