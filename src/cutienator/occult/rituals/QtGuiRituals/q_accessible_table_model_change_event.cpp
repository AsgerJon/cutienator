//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <cstring>

//  A QAccessibleTableModelChangeEvent that Python can take functions over in. Every QAccessibleTableModelChangeEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQAccessibleTableModelChangeEventCall0)(const void *, int *);
class CuteQAccessibleTableModelChangeEvent : public QAccessibleTableModelChangeEvent {
public:
  using QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QAccessibleEvent19accessibleInterfaceEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QAccessibleInterface *QAccessibleEvent::accessibleInterface() const
  QAccessibleInterface *accessibleInterface() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleTableModelChangeEventCall0 call = reinterpret_cast<CuteQAccessibleTableModelChangeEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QAccessibleEvent::accessibleInterface();
  }
};

//  QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent(QObjec
//      t *obj, ModelChangeType changeType)
extern "C" Q_DECL_EXPORT
QAccessibleTableModelChangeEvent *ritual_ZN32QAccessibleTableModelChangeEventC1EP7QObjectNS_15ModelChangeTypeE(
    QObject *obj,
    QAccessibleTableModelChangeEvent::ModelChangeType changeType) {
  return new CuteQAccessibleTableModelChangeEvent(obj, changeType);
}

//  QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent(QAcces
//      sibleInterface *iface, ModelChangeType changeType)
extern "C" Q_DECL_EXPORT
QAccessibleTableModelChangeEvent *ritual_ZN32QAccessibleTableModelChangeEventC1EP20QAccessibleInterfaceNS_15ModelChangeTypeE(
    QAccessibleInterface *iface,
    QAccessibleTableModelChangeEvent::ModelChangeType changeType) {
  return new CuteQAccessibleTableModelChangeEvent(iface, changeType);
}

//  QAccessibleTableModelChangeEvent::~QAccessibleTableModelChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleTableModelChangeEventD1Ev(
    QAccessibleTableModelChangeEvent *self) {
  delete self;
}

//  void QAccessibleTableModelChangeEvent::setModelChangeType(ModelChangeType
//      changeType)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleTableModelChangeEvent18setModelChangeTypeENS_15ModelChangeTypeE(
    QAccessibleTableModelChangeEvent *self,
    QAccessibleTableModelChangeEvent::ModelChangeType changeType) {
  self->setModelChangeType(changeType);
}

//  ModelChangeType QAccessibleTableModelChangeEvent::modelChangeType() const
extern "C" Q_DECL_EXPORT
QAccessibleTableModelChangeEvent::ModelChangeType ritual_ZNK32QAccessibleTableModelChangeEvent15modelChangeTypeEv(
    const QAccessibleTableModelChangeEvent *self) {
  return self->modelChangeType();
}

//  void QAccessibleTableModelChangeEvent::setFirstRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleTableModelChangeEvent11setFirstRowEi(
    QAccessibleTableModelChangeEvent *self,
    int row) {
  self->setFirstRow(row);
}

//  void QAccessibleTableModelChangeEvent::setFirstColumn(int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleTableModelChangeEvent14setFirstColumnEi(
    QAccessibleTableModelChangeEvent *self,
    int col) {
  self->setFirstColumn(col);
}

//  void QAccessibleTableModelChangeEvent::setLastRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleTableModelChangeEvent10setLastRowEi(
    QAccessibleTableModelChangeEvent *self,
    int row) {
  self->setLastRow(row);
}

//  void QAccessibleTableModelChangeEvent::setLastColumn(int col)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QAccessibleTableModelChangeEvent13setLastColumnEi(
    QAccessibleTableModelChangeEvent *self,
    int col) {
  self->setLastColumn(col);
}

//  int QAccessibleTableModelChangeEvent::firstRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QAccessibleTableModelChangeEvent8firstRowEv(
    const QAccessibleTableModelChangeEvent *self) {
  return self->firstRow();
}

//  int QAccessibleTableModelChangeEvent::firstColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QAccessibleTableModelChangeEvent11firstColumnEv(
    const QAccessibleTableModelChangeEvent *self) {
  return self->firstColumn();
}

//  int QAccessibleTableModelChangeEvent::lastRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QAccessibleTableModelChangeEvent7lastRowEv(
    const QAccessibleTableModelChangeEvent *self) {
  return self->lastRow();
}

//  int QAccessibleTableModelChangeEvent::lastColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QAccessibleTableModelChangeEvent10lastColumnEv(
    const QAccessibleTableModelChangeEvent *self) {
  return self->lastColumn();
}

//  a Python function taken by a CuteQAccessibleTableModelChangeEvent, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleTableModelChangeEvent(
    QAccessibleTableModelChangeEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleTableModelChangeEvent *>(self)->take(key, call);
}
