//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>

//  QAccessibleSelectionInterface::~QAccessibleSelectionInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleSelectionInterfaceD1Ev(
    QAccessibleSelectionInterface *self) {
  delete self;
}

//  int QAccessibleSelectionInterface::selectedItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleSelectionInterface17selectedItemCountEv(
    const QAccessibleSelectionInterface *self) {
  return self->selectedItemCount();
}

//  QAccessibleInterface *QAccessibleSelectionInterface::selectedItem(int
//      selectionIndex) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK29QAccessibleSelectionInterface12selectedItemEi(
    const QAccessibleSelectionInterface *self,
    int selectionIndex) {
  return self->selectedItem(selectionIndex);
}

//  bool QAccessibleSelectionInterface::isSelected(QAccessibleInterface
//      *childItem) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleSelectionInterface10isSelectedEP20QAccessibleInterface(
    const QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->isSelected(childItem);
}

//  bool QAccessibleSelectionInterface::select(QAccessibleInterface
//      *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface6selectEP20QAccessibleInterface(
    QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->select(childItem);
}

//  bool QAccessibleSelectionInterface::unselect(QAccessibleInterface
//      *childItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface8unselectEP20QAccessibleInterface(
    QAccessibleSelectionInterface *self,
    QAccessibleInterface *childItem) {
  return self->unselect(childItem);
}

//  bool QAccessibleSelectionInterface::selectAll()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface9selectAllEv(
    QAccessibleSelectionInterface *self) {
  return self->selectAll();
}

//  bool QAccessibleSelectionInterface::clear()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QAccessibleSelectionInterface5clearEv(
    QAccessibleSelectionInterface *self) {
  return self->clear();
}
