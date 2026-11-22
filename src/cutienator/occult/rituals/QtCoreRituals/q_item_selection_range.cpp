//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qabstractitemmodel.h>

//  QItemSelectionRange::QItemSelectionRange()
extern "C" Q_DECL_EXPORT
QItemSelectionRange *ritual_ZN19QItemSelectionRangeC1Ev() {
  return new QItemSelectionRange();
}

//  QItemSelectionRange::QItemSelectionRange(const QModelIndex &topL, const
//      QModelIndex &bottomR)
extern "C" Q_DECL_EXPORT
QItemSelectionRange *ritual_ZN19QItemSelectionRangeC1ERK11QModelIndexS2_(
    const QModelIndex *topL,
    const QModelIndex *bottomR) {
  return new QItemSelectionRange(*topL, *bottomR);
}

//  QItemSelectionRange::QItemSelectionRange(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
QItemSelectionRange *ritual_ZN19QItemSelectionRangeC1ERK11QModelIndex(
    const QModelIndex *index) {
  return new QItemSelectionRange(*index);
}

//  int QItemSelectionRange::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QItemSelectionRange3topEv(const QItemSelectionRange *self) {
  return self->top();
}

//  int QItemSelectionRange::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QItemSelectionRange4leftEv(const QItemSelectionRange *self) {
  return self->left();
}

//  int QItemSelectionRange::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QItemSelectionRange6bottomEv(
    const QItemSelectionRange *self) {
  return self->bottom();
}

//  int QItemSelectionRange::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QItemSelectionRange5rightEv(
    const QItemSelectionRange *self) {
  return self->right();
}

//  int QItemSelectionRange::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QItemSelectionRange5widthEv(
    const QItemSelectionRange *self) {
  return self->width();
}

//  int QItemSelectionRange::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QItemSelectionRange6heightEv(
    const QItemSelectionRange *self) {
  return self->height();
}

//  const QPersistentModelIndex &QItemSelectionRange::topLeft() const
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZNK19QItemSelectionRange7topLeftEv(
    const QItemSelectionRange *self) {
  return new QPersistentModelIndex(self->topLeft());
}

//  const QPersistentModelIndex &QItemSelectionRange::bottomRight() const
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZNK19QItemSelectionRange11bottomRightEv(
    const QItemSelectionRange *self) {
  return new QPersistentModelIndex(self->bottomRight());
}

//  QModelIndex QItemSelectionRange::parent() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QItemSelectionRange6parentEv(
    const QItemSelectionRange *self) {
  return new QModelIndex(self->parent());
}

//  const QAbstractItemModel *QItemSelectionRange::model() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK19QItemSelectionRange5modelEv(
    const QItemSelectionRange *self) {
  return self->model();
}

//  bool QItemSelectionRange::contains(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionRange8containsERK11QModelIndex(
    const QItemSelectionRange *self,
    const QModelIndex *index) {
  return self->contains(*index);
}

//  bool QItemSelectionRange::contains(int row, int column, const QModelIndex
//      &parentIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionRange8containsEiiRK11QModelIndex(
    const QItemSelectionRange *self,
    int row,
    int column,
    const QModelIndex *parentIndex) {
  return self->contains(row, column, *parentIndex);
}

//  bool QItemSelectionRange::intersects(const QItemSelectionRange &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionRange10intersectsERKS_(
    const QItemSelectionRange *self,
    const QItemSelectionRange *other) {
  return self->intersects(*other);
}

//  QItemSelectionRange QItemSelectionRange::intersected(const
//      QItemSelectionRange &other) const
extern "C" Q_DECL_EXPORT
QItemSelectionRange *ritual_ZNK19QItemSelectionRange11intersectedERKS_(
    const QItemSelectionRange *self,
    const QItemSelectionRange *other) {
  return new QItemSelectionRange(self->intersected(*other));
}

//  bool QItemSelectionRange::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionRange7isValidEv(
    const QItemSelectionRange *self) {
  return self->isValid();
}

//  bool QItemSelectionRange::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionRange7isEmptyEv(
    const QItemSelectionRange *self) {
  return self->isEmpty();
}

//  bool operator==(const QItemSelectionRange &lhs, const QItemSelectionRange
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QItemSelectionRangeS1_(
    const QItemSelectionRange *lhs,
    const QItemSelectionRange *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QItemSelectionRange &lhs, const QItemSelectionRange
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QItemSelectionRangeS1_(
    const QItemSelectionRange *lhs,
    const QItemSelectionRange *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QItemSelectionRange::~QItemSelectionRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionRangeD1Ev(QItemSelectionRange *self) {
  delete self;
}
