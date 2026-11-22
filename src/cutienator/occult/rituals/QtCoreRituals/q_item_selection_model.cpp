//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QItemSelectionModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QItemSelectionModel10metaObjectEv(
    const QItemSelectionModel *self) {
  return self->metaObject();
}

//  QString QItemSelectionModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QItemSelectionModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemSelectionModel::tr(s, c, n));
}

//  QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZN19QItemSelectionModelC1EP18QAbstractItemModel(
    QAbstractItemModel *model) {
  return new QItemSelectionModel(model);
}

//  QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZN19QItemSelectionModelC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *model,
    QObject *parent) {
  return new QItemSelectionModel(model, parent);
}

//  QItemSelectionModel::~QItemSelectionModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModelD1Ev(QItemSelectionModel *self) {
  delete self;
}

//  QModelIndex QItemSelectionModel::currentIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QItemSelectionModel12currentIndexEv(
    const QItemSelectionModel *self) {
  return new QModelIndex(self->currentIndex());
}

//  bool QItemSelectionModel::isSelected(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionModel10isSelectedERK11QModelIndex(
    const QItemSelectionModel *self,
    const QModelIndex *index) {
  return self->isSelected(*index);
}

//  bool QItemSelectionModel::isRowSelected(int row, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionModel13isRowSelectedEiRK11QModelIndex(
    const QItemSelectionModel *self,
    int row,
    const QModelIndex *parent) {
  return self->isRowSelected(row, *parent);
}

//  bool QItemSelectionModel::isColumnSelected(int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionModel16isColumnSelectedEiRK11QModelIndex(
    const QItemSelectionModel *self,
    int column,
    const QModelIndex *parent) {
  return self->isColumnSelected(column, *parent);
}

//  bool QItemSelectionModel::rowIntersectsSelection(int row, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionModel22rowIntersectsSelectionEiRK11QModelIndex(
    const QItemSelectionModel *self,
    int row,
    const QModelIndex *parent) {
  return self->rowIntersectsSelection(row, *parent);
}

//  bool QItemSelectionModel::columnIntersectsSelection(int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionModel25columnIntersectsSelectionEiRK11QModelIndex(
    const QItemSelectionModel *self,
    int column,
    const QModelIndex *parent) {
  return self->columnIntersectsSelection(column, *parent);
}

//  bool QItemSelectionModel::hasSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QItemSelectionModel12hasSelectionEv(
    const QItemSelectionModel *self) {
  return self->hasSelection();
}

//  const QItemSelection QItemSelectionModel::selection() const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QItemSelectionModel9selectionEv(
    const QItemSelectionModel *self) {
  return new QItemSelection(self->selection());
}

//  const QAbstractItemModel *QItemSelectionModel::model() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK19QItemSelectionModel5modelEv(
    const QItemSelectionModel *self) {
  return self->model();
}

//  QAbstractItemModel *QItemSelectionModel::model()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN19QItemSelectionModel5modelEv(
    QItemSelectionModel *self) {
  return self->model();
}

//  void QItemSelectionModel::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel8setModelEP18QAbstractItemModel(
    QItemSelectionModel *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  void QItemSelectionModel::setCurrentIndex(const QModelIndex &index,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel15setCurrentIndexERK11QModelIndex6QFlagsINS_13SelectionFlagEE(
    QItemSelectionModel *self,
    const QModelIndex *index,
    int command) {
  self->setCurrentIndex(
      *index,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelectionModel::select(const QModelIndex &index,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel6selectERK11QModelIndex6QFlagsINS_13SelectionFlagEE(
    QItemSelectionModel *self,
    const QModelIndex *index,
    int command) {
  self->select(
      *index,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelectionModel::select(const QItemSelection &selection,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel6selectERK14QItemSelection6QFlagsINS_13SelectionFlagEE(
    QItemSelectionModel *self,
    const QItemSelection *selection,
    int command) {
  self->select(
      *selection,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelectionModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel5clearEv(QItemSelectionModel *self) {
  self->clear();
}

//  void QItemSelectionModel::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel5resetEv(QItemSelectionModel *self) {
  self->reset();
}

//  void QItemSelectionModel::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel14clearSelectionEv(
    QItemSelectionModel *self) {
  self->clearSelection();
}

//  void QItemSelectionModel::clearCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel17clearCurrentIndexEv(
    QItemSelectionModel *self) {
  self->clearCurrentIndex();
}
