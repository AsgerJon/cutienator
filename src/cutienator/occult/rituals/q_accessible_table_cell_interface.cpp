//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>

//  QAccessibleTableCellInterface::~QAccessibleTableCellInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleTableCellInterfaceD1Ev(
    QAccessibleTableCellInterface *self) {
  delete self;
}

//  bool QAccessibleTableCellInterface::isSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleTableCellInterface10isSelectedEv(
    const QAccessibleTableCellInterface *self) {
  return self->isSelected();
}

//  int QAccessibleTableCellInterface::columnIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface11columnIndexEv(
    const QAccessibleTableCellInterface *self) {
  return self->columnIndex();
}

//  int QAccessibleTableCellInterface::rowIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface8rowIndexEv(
    const QAccessibleTableCellInterface *self) {
  return self->rowIndex();
}

//  int QAccessibleTableCellInterface::columnExtent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface12columnExtentEv(
    const QAccessibleTableCellInterface *self) {
  return self->columnExtent();
}

//  int QAccessibleTableCellInterface::rowExtent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleTableCellInterface9rowExtentEv(
    const QAccessibleTableCellInterface *self) {
  return self->rowExtent();
}

//  QAccessibleInterface *QAccessibleTableCellInterface::table() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QAccessibleTableCellInterface5tableEv(
    const QAccessibleTableCellInterface *self) {
  return self->table();
}
