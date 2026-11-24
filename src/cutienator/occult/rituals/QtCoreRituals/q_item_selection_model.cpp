//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qitemselectionmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QItemSelectionModel that Python can take functions over in. Every QItemSelectionModel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemmodel)
typedef void (*CuteQItemSelectionModelCall0)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQItemSelectionModelCall1)(const void *, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQItemSelectionModelCall2)(const void *, const QItemSelection *, int, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQItemSelectionModelCall3)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQItemSelectionModelCall4)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
typedef void (*CuteQItemSelectionModelCall5)(const void *, int *);
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemSelectionModelCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQItemSelectionModelCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemSelectionModelCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemSelectionModelCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemSelectionModelCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemSelectionModelCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQItemSelectionModelCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQItemSelectionModel : public QItemSelectionModel {
public:
  using QItemSelectionModel::QItemSelectionModel;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN19QItemSelectionModel15setCurrentIndexERK11QModelIndex6QFlagsINS_13SelectionFlagEE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN19QItemSelectionModel6selectERK11QModelIndex6QFlagsINS_13SelectionFlagEE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN19QItemSelectionModel6selectERK14QItemSelection6QFlagsINS_13SelectionFlagEE")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN19QItemSelectionModel5clearEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN19QItemSelectionModel5resetEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
    if (!std::strcmp(key, "_ZN19QItemSelectionModel17clearCurrentIndexEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemmodel)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(itemmodel)
  //  void QItemSelectionModel::setCurrentIndex(const QModelIndex &index,
  //      QItemSelectionModel::SelectionFlags command)
  void setCurrentIndex(
      const QModelIndex &index,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[0]) {
      int handled = 0;
      CuteQItemSelectionModelCall0 call = reinterpret_cast<CuteQItemSelectionModelCall0>(taken[0]);
      call(this, &index, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QItemSelectionModel::setCurrentIndex(index, command);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QItemSelectionModel::select(const QModelIndex &index,
  //      QItemSelectionModel::SelectionFlags command)
  void select(
      const QModelIndex &index,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[1]) {
      int handled = 0;
      CuteQItemSelectionModelCall1 call = reinterpret_cast<CuteQItemSelectionModelCall1>(taken[1]);
      call(this, &index, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QItemSelectionModel::select(index, command);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QItemSelectionModel::select(const QItemSelection &selection,
  //      QItemSelectionModel::SelectionFlags command)
  void select(
      const QItemSelection &selection,
      QItemSelectionModel::SelectionFlags command) override {
    if (taken[2]) {
      int handled = 0;
      CuteQItemSelectionModelCall2 call = reinterpret_cast<CuteQItemSelectionModelCall2>(taken[2]);
      call(this, &selection, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QItemSelectionModel::select(selection, command);
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QItemSelectionModel::clear()
  void clear() override {
    if (taken[3]) {
      int handled = 0;
      CuteQItemSelectionModelCall3 call = reinterpret_cast<CuteQItemSelectionModelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QItemSelectionModel::clear();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QItemSelectionModel::reset()
  void reset() override {
    if (taken[4]) {
      int handled = 0;
      CuteQItemSelectionModelCall4 call = reinterpret_cast<CuteQItemSelectionModelCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QItemSelectionModel::reset();
  }
#endif  // QT_CONFIG(itemmodel)

#if QT_CONFIG(itemmodel)
  //  void QItemSelectionModel::clearCurrentIndex()
  void clearCurrentIndex() override {
    if (taken[5]) {
      int handled = 0;
      CuteQItemSelectionModelCall5 call = reinterpret_cast<CuteQItemSelectionModelCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QItemSelectionModel::clearCurrentIndex();
  }
#endif  // QT_CONFIG(itemmodel)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQItemSelectionModelCall6 call = reinterpret_cast<CuteQItemSelectionModelCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQItemSelectionModelCall7 call = reinterpret_cast<CuteQItemSelectionModelCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQItemSelectionModelCall8 call = reinterpret_cast<CuteQItemSelectionModelCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQItemSelectionModelCall9 call = reinterpret_cast<CuteQItemSelectionModelCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQItemSelectionModelCall10 call = reinterpret_cast<CuteQItemSelectionModelCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQItemSelectionModelCall11 call = reinterpret_cast<CuteQItemSelectionModelCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQItemSelectionModelCall12 call = reinterpret_cast<CuteQItemSelectionModelCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

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

//  QItemSelectionModelPrivate *QItemSelectionModel::d_func()
extern "C" Q_DECL_EXPORT
QItemSelectionModelPrivate *ritual_ZN19QItemSelectionModel6d_funcEv(
    QItemSelectionModel *self) {
  return self->d_func();
}

//  const QItemSelectionModelPrivate *QItemSelectionModel::d_func() const
extern "C" Q_DECL_EXPORT
const QItemSelectionModelPrivate *ritual_ZNK19QItemSelectionModel6d_funcEv(
    const QItemSelectionModel *self) {
  return self->d_func();
}

//  QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZN19QItemSelectionModelC1EP18QAbstractItemModel(
    QAbstractItemModel *model) {
  return new CuteQItemSelectionModel(model);
}

//  QItemSelectionModel::QItemSelectionModel(QAbstractItemModel *model,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QItemSelectionModel *ritual_ZN19QItemSelectionModelC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *model,
    QObject *parent) {
  return new CuteQItemSelectionModel(model, parent);
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

//  QModelIndexList QItemSelectionModel::selectedIndexes() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK19QItemSelectionModel15selectedIndexesEv(
    const QItemSelectionModel *self) {
  return new QList<QModelIndex>(self->selectedIndexes());
}

//  QModelIndexList QItemSelectionModel::selectedRows(int column) const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK19QItemSelectionModel12selectedRowsEi(
    const QItemSelectionModel *self,
    int column) {
  return new QList<QModelIndex>(self->selectedRows(column));
}

//  QModelIndexList QItemSelectionModel::selectedColumns(int row) const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK19QItemSelectionModel15selectedColumnsEi(
    const QItemSelectionModel *self,
    int row) {
  return new QList<QModelIndex>(self->selectedColumns(row));
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

//  void QItemSelectionModel::emitSelectionChanged(const QItemSelection
//      &newSelection, const QItemSelection &oldSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QItemSelectionModel20emitSelectionChangedERK14QItemSelectionS2_(
    QItemSelectionModel *self,
    const QItemSelection *newSelection,
    const QItemSelection *oldSelection) {
  self->emitSelectionChanged(*newSelection, *oldSelection);
}

//  a Python function taken by a CuteQItemSelectionModel, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QItemSelectionModel(
    QItemSelectionModel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQItemSelectionModel *>(self)->take(key, call);
}

//  void QItemSelectionModel::setCurrentIndex(const QModelIndex &index,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QItemSelectionModel15setCurrentIndexERK11QModelIndex6QFlagsINS_13SelectionFlagEE(
    QItemSelectionModel *self,
    const QModelIndex *index,
    int command) {
  self->QItemSelectionModel::setCurrentIndex(
      *index,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelectionModel::select(const QModelIndex &index,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QItemSelectionModel6selectERK11QModelIndex6QFlagsINS_13SelectionFlagEE(
    QItemSelectionModel *self,
    const QModelIndex *index,
    int command) {
  self->QItemSelectionModel::select(
      *index,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelectionModel::select(const QItemSelection &selection,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QItemSelectionModel6selectERK14QItemSelection6QFlagsINS_13SelectionFlagEE(
    QItemSelectionModel *self,
    const QItemSelection *selection,
    int command) {
  self->QItemSelectionModel::select(
      *selection,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QItemSelectionModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QItemSelectionModel5clearEv(QItemSelectionModel *self) {
  self->QItemSelectionModel::clear();
}

//  void QItemSelectionModel::reset()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QItemSelectionModel5resetEv(QItemSelectionModel *self) {
  self->QItemSelectionModel::reset();
}

//  void QItemSelectionModel::clearCurrentIndex()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QItemSelectionModel17clearCurrentIndexEv(
    QItemSelectionModel *self) {
  self->QItemSelectionModel::clearCurrentIndex();
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
