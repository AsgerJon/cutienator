//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtablewidget.h>
#include <QtCore/qlist.h>

//  QTableWidgetSelectionRange::QTableWidgetSelectionRange()
extern "C" Q_DECL_EXPORT
QTableWidgetSelectionRange *ritual_ZN26QTableWidgetSelectionRangeC1Ev() {
  return new QTableWidgetSelectionRange();
}

//  QTableWidgetSelectionRange::QTableWidgetSelectionRange(int top, int left,
//      int bottom, int right)
extern "C" Q_DECL_EXPORT
QTableWidgetSelectionRange *ritual_ZN26QTableWidgetSelectionRangeC1Eiiii(
    int top,
    int left,
    int bottom,
    int right) {
  return new QTableWidgetSelectionRange(top, left, bottom, right);
}

//  bool operator==(const QTableWidgetSelectionRange &lhs, const
//      QTableWidgetSelectionRange &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK26QTableWidgetSelectionRangeS1_(
    const QTableWidgetSelectionRange *lhs,
    const QTableWidgetSelectionRange *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QTableWidgetSelectionRange &lhs, const
//      QTableWidgetSelectionRange &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK26QTableWidgetSelectionRangeS1_(
    const QTableWidgetSelectionRange *lhs,
    const QTableWidgetSelectionRange *rhs) {
  return operator!=(*lhs, *rhs);
}

//  int QTableWidgetSelectionRange::topRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QTableWidgetSelectionRange6topRowEv(
    const QTableWidgetSelectionRange *self) {
  return self->topRow();
}

//  int QTableWidgetSelectionRange::bottomRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QTableWidgetSelectionRange9bottomRowEv(
    const QTableWidgetSelectionRange *self) {
  return self->bottomRow();
}

//  int QTableWidgetSelectionRange::leftColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QTableWidgetSelectionRange10leftColumnEv(
    const QTableWidgetSelectionRange *self) {
  return self->leftColumn();
}

//  int QTableWidgetSelectionRange::rightColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QTableWidgetSelectionRange11rightColumnEv(
    const QTableWidgetSelectionRange *self) {
  return self->rightColumn();
}

//  int QTableWidgetSelectionRange::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QTableWidgetSelectionRange8rowCountEv(
    const QTableWidgetSelectionRange *self) {
  return self->rowCount();
}

//  int QTableWidgetSelectionRange::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QTableWidgetSelectionRange11columnCountEv(
    const QTableWidgetSelectionRange *self) {
  return self->columnCount();
}

//  QTableWidgetSelectionRange::~QTableWidgetSelectionRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QTableWidgetSelectionRangeD1Ev(
    QTableWidgetSelectionRange *self) {
  delete self;
}

//  QList<QTableWidgetSelectionRange>::QList()
extern "C" Q_DECL_EXPORT
QList<QTableWidgetSelectionRange> *ritual_list_make_QTableWidgetSelectionRange() {
  return new QList<QTableWidgetSelectionRange>();
}

//  void QList<QTableWidgetSelectionRange>::append(const
//      QTableWidgetSelectionRange &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QTableWidgetSelectionRange(
    QList<QTableWidgetSelectionRange> *self,
    const QTableWidgetSelectionRange *element) {
  self->append(*element);
}

//  qsizetype QList<QTableWidgetSelectionRange>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QTableWidgetSelectionRange(
    const QList<QTableWidgetSelectionRange> *self) {
  return self->size();
}

//  const QTableWidgetSelectionRange
//      &QList<QTableWidgetSelectionRange>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QTableWidgetSelectionRange *ritual_list_at_QTableWidgetSelectionRange(
    const QList<QTableWidgetSelectionRange> *self,
    long long index) {
  return new QTableWidgetSelectionRange(self->at(index));
}

//  QList<QTableWidgetSelectionRange>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QTableWidgetSelectionRange(
    QList<QTableWidgetSelectionRange> *self) {
  delete self;
}
