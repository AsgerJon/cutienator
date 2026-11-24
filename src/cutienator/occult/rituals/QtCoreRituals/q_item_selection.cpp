//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qlist.h>

//  QItemSelection::QItemSelection(const QModelIndex &topLeft, const
//      QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZN14QItemSelectionC1ERK11QModelIndexS2_(
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QItemSelection(*topLeft, *bottomRight);
}

//  void QItemSelection::select(const QModelIndex &topLeft, const QModelIndex
//      &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QItemSelection6selectERK11QModelIndexS2_(
    QItemSelection *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->select(*topLeft, *bottomRight);
}

//  bool QItemSelection::contains(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QItemSelection8containsERK11QModelIndex(
    const QItemSelection *self,
    const QModelIndex *index) {
  return self->contains(*index);
}

//  QModelIndexList QItemSelection::indexes() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK14QItemSelection7indexesEv(
    const QItemSelection *self) {
  return new QList<QModelIndex>(self->indexes());
}

//  void QItemSelection::merge(const QItemSelection &other,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QItemSelection5mergeERKS_6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QItemSelection *self,
    const QItemSelection *other,
    int command) {
  self->merge(
      *other,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelection::split(const QItemSelectionRange &range, const
//      QItemSelectionRange &other, QItemSelection *result)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QItemSelection5splitERK19QItemSelectionRangeS2_PS_(
    const QItemSelectionRange *range,
    const QItemSelectionRange *other,
    QItemSelection *result) {
  QItemSelection::split(*range, *other, result);
}

//  QItemSelection::~QItemSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QItemSelectionD1Ev(QItemSelection *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
