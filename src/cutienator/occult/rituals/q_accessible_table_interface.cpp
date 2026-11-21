//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>

//  QAccessibleTableInterface::~QAccessibleTableInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleTableInterfaceD1Ev(
    QAccessibleTableInterface *self) {
  delete self;
}

//  QAccessibleInterface *QAccessibleTableInterface::caption() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleTableInterface7captionEv(
    const QAccessibleTableInterface *self) {
  return self->caption();
}

//  QAccessibleInterface *QAccessibleTableInterface::summary() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleTableInterface7summaryEv(
    const QAccessibleTableInterface *self) {
  return self->summary();
}

//  QAccessibleInterface *QAccessibleTableInterface::cellAt(int row, int
//      column) const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK25QAccessibleTableInterface6cellAtEii(
    const QAccessibleTableInterface *self,
    int row,
    int column) {
  return self->cellAt(row, column);
}

//  int QAccessibleTableInterface::selectedCellCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface17selectedCellCountEv(
    const QAccessibleTableInterface *self) {
  return self->selectedCellCount();
}

//  QString QAccessibleTableInterface::columnDescription(int column) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAccessibleTableInterface17columnDescriptionEi(
    const QAccessibleTableInterface *self,
    int column) {
  return new QString(self->columnDescription(column));
}

//  QString QAccessibleTableInterface::rowDescription(int row) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAccessibleTableInterface14rowDescriptionEi(
    const QAccessibleTableInterface *self,
    int row) {
  return new QString(self->rowDescription(row));
}

//  int QAccessibleTableInterface::selectedColumnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface19selectedColumnCountEv(
    const QAccessibleTableInterface *self) {
  return self->selectedColumnCount();
}

//  int QAccessibleTableInterface::selectedRowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface16selectedRowCountEv(
    const QAccessibleTableInterface *self) {
  return self->selectedRowCount();
}

//  int QAccessibleTableInterface::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface11columnCountEv(
    const QAccessibleTableInterface *self) {
  return self->columnCount();
}

//  int QAccessibleTableInterface::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QAccessibleTableInterface8rowCountEv(
    const QAccessibleTableInterface *self) {
  return self->rowCount();
}

//  bool QAccessibleTableInterface::isColumnSelected(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAccessibleTableInterface16isColumnSelectedEi(
    const QAccessibleTableInterface *self,
    int column) {
  return self->isColumnSelected(column);
}

//  bool QAccessibleTableInterface::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QAccessibleTableInterface13isRowSelectedEi(
    const QAccessibleTableInterface *self,
    int row) {
  return self->isRowSelected(row);
}

//  bool QAccessibleTableInterface::selectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface9selectRowEi(
    QAccessibleTableInterface *self,
    int row) {
  return self->selectRow(row);
}

//  bool QAccessibleTableInterface::selectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface12selectColumnEi(
    QAccessibleTableInterface *self,
    int column) {
  return self->selectColumn(column);
}

//  bool QAccessibleTableInterface::unselectRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface11unselectRowEi(
    QAccessibleTableInterface *self,
    int row) {
  return self->unselectRow(row);
}

//  bool QAccessibleTableInterface::unselectColumn(int column)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAccessibleTableInterface14unselectColumnEi(
    QAccessibleTableInterface *self,
    int column) {
  return self->unselectColumn(column);
}

//  void
//      QAccessibleTableInterface::modelChange(QAccessibleTableModelChangeEve
//      nt *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleTableInterface11modelChangeEP32QAccessibleTableModelChangeEvent(
    QAccessibleTableInterface *self,
    QAccessibleTableModelChangeEvent *event) {
  self->modelChange(event);
}
