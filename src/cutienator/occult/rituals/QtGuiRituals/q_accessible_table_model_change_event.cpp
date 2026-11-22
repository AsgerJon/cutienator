//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>

//  QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent(QObjec
//      t *obj, ModelChangeType changeType)
extern "C" Q_DECL_EXPORT
QAccessibleTableModelChangeEvent *ritual_ZN32QAccessibleTableModelChangeEventC1EP7QObjectNS_15ModelChangeTypeE(
    QObject *obj,
    QAccessibleTableModelChangeEvent::ModelChangeType changeType) {
  return new QAccessibleTableModelChangeEvent(obj, changeType);
}

//  QAccessibleTableModelChangeEvent::QAccessibleTableModelChangeEvent(QAcces
//      sibleInterface *iface, ModelChangeType changeType)
extern "C" Q_DECL_EXPORT
QAccessibleTableModelChangeEvent *ritual_ZN32QAccessibleTableModelChangeEventC1EP20QAccessibleInterfaceNS_15ModelChangeTypeE(
    QAccessibleInterface *iface,
    QAccessibleTableModelChangeEvent::ModelChangeType changeType) {
  return new QAccessibleTableModelChangeEvent(iface, changeType);
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
