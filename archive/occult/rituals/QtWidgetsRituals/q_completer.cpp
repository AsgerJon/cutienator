//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcompleter.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcompleter.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QCompleter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCompleter : QCompleter {
  using QCompleter::eventFilter;
  using QCompleter::event;
};

//  A QCompleter that Python can take functions over in. Every QCompleter
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQCompleterCall0)(const void *, const QModelIndex *, int *);
typedef bool (*CuteQCompleterCall1)(const void *, QObject *, QEvent *, int *);
typedef bool (*CuteQCompleterCall2)(const void *, QEvent *, int *);
typedef void (*CuteQCompleterCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQCompleterCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQCompleterCall5)(const void *, QEvent *, int *);
typedef void (*CuteQCompleterCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQCompleterCall7)(const void *, const QMetaMethod *, int *);
class CuteQCompleter : public QCompleter {
public:
  using QCompleter::QCompleter;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QCompleter13pathFromIndexERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QString QCompleter::pathFromIndex(const QModelIndex &index) const
  QString pathFromIndex(const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCompleterCall0 call = reinterpret_cast<CuteQCompleterCall0>(taken[0]);
      QString * given = call(this, &index, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QCompleter::pathFromIndex(index);
  }

  //  bool QCompleter::eventFilter(QObject *o, QEvent *e)
  bool eventFilter(QObject *o, QEvent *e) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCompleterCall1 call = reinterpret_cast<CuteQCompleterCall1>(taken[1]);
      bool given = call(this, o, e, &handled);
      if (handled) return given;
    }
    return QCompleter::eventFilter(o, e);
  }

  //  bool QCompleter::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCompleterCall2 call = reinterpret_cast<CuteQCompleterCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCompleter::event(a0);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCompleterCall3 call = reinterpret_cast<CuteQCompleterCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCompleterCall4 call = reinterpret_cast<CuteQCompleterCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCompleterCall5 call = reinterpret_cast<CuteQCompleterCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCompleterCall6 call = reinterpret_cast<CuteQCompleterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQCompleterCall7 call = reinterpret_cast<CuteQCompleterCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QCompleter::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QCompleter10metaObjectEv(
    const QCompleter *self) {
  return self->metaObject();
}

//  QString QCompleter::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QCompleter2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCompleter::tr(s, c, n));
}

//  QCompleter::QCompleter(QObject *parent)
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN10QCompleterC1EP7QObject(QObject *parent) {
  return new CuteQCompleter(parent);
}

//  QCompleter::QCompleter(QAbstractItemModel *model, QObject *parent)
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN10QCompleterC1EP18QAbstractItemModelP7QObject(
    QAbstractItemModel *model,
    QObject *parent) {
  return new CuteQCompleter(model, parent);
}

//  QCompleter::QCompleter(const QStringList &completions, QObject *parent)
extern "C" Q_DECL_EXPORT
QCompleter *ritual_ZN10QCompleterC1ERK5QListI7QStringEP7QObject(
    const QList<QString> *completions,
    QObject *parent) {
  return new CuteQCompleter(*completions, parent);
}

//  QCompleter::~QCompleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleterD1Ev(QCompleter *self) {
  delete self;
}

//  void QCompleter::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter9setWidgetEP7QWidget(
    QCompleter *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QCompleter::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK10QCompleter6widgetEv(const QCompleter *self) {
  return self->widget();
}

//  void QCompleter::setModel(QAbstractItemModel *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter8setModelEP18QAbstractItemModel(
    QCompleter *self,
    QAbstractItemModel *c) {
  self->setModel(c);
}

//  QAbstractItemModel *QCompleter::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK10QCompleter5modelEv(const QCompleter *self) {
  return self->model();
}

//  void QCompleter::setCompletionMode(CompletionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter17setCompletionModeENS_14CompletionModeE(
    QCompleter *self,
    QCompleter::CompletionMode mode) {
  self->setCompletionMode(mode);
}

//  CompletionMode QCompleter::completionMode() const
extern "C" Q_DECL_EXPORT
QCompleter::CompletionMode ritual_ZNK10QCompleter14completionModeEv(
    const QCompleter *self) {
  return self->completionMode();
}

//  void QCompleter::setFilterMode(Qt::MatchFlags filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter13setFilterModeE6QFlagsIN2Qt9MatchFlagEE(
    QCompleter *self,
    int filterMode) {
  self->setFilterMode(QFlags<Qt::MatchFlag>::fromInt(filterMode));
}

//  Qt::MatchFlags QCompleter::filterMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter10filterModeEv(const QCompleter *self) {
  return static_cast<int>(self->filterMode().toInt());
}

//  QAbstractItemView *QCompleter::popup() const
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZNK10QCompleter5popupEv(const QCompleter *self) {
  return self->popup();
}

//  void QCompleter::setPopup(QAbstractItemView *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter8setPopupEP17QAbstractItemView(
    QCompleter *self,
    QAbstractItemView *popup) {
  self->setPopup(popup);
}

//  void QCompleter::setCaseSensitivity(Qt::CaseSensitivity caseSensitivity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter18setCaseSensitivityEN2Qt15CaseSensitivityE(
    QCompleter *self,
    Qt::CaseSensitivity caseSensitivity) {
  self->setCaseSensitivity(caseSensitivity);
}

//  Qt::CaseSensitivity QCompleter::caseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK10QCompleter15caseSensitivityEv(
    const QCompleter *self) {
  return self->caseSensitivity();
}

//  void QCompleter::setModelSorting(ModelSorting sorting)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter15setModelSortingENS_12ModelSortingE(
    QCompleter *self,
    QCompleter::ModelSorting sorting) {
  self->setModelSorting(sorting);
}

//  ModelSorting QCompleter::modelSorting() const
extern "C" Q_DECL_EXPORT
QCompleter::ModelSorting ritual_ZNK10QCompleter12modelSortingEv(
    const QCompleter *self) {
  return self->modelSorting();
}

//  void QCompleter::setCompletionColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter19setCompletionColumnEi(
    QCompleter *self,
    int column) {
  self->setCompletionColumn(column);
}

//  int QCompleter::completionColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter16completionColumnEv(const QCompleter *self) {
  return self->completionColumn();
}

//  void QCompleter::setCompletionRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter17setCompletionRoleEi(QCompleter *self, int role) {
  self->setCompletionRole(role);
}

//  int QCompleter::completionRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter14completionRoleEv(const QCompleter *self) {
  return self->completionRole();
}

//  bool QCompleter::wrapAround() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QCompleter10wrapAroundEv(const QCompleter *self) {
  return self->wrapAround();
}

//  int QCompleter::maxVisibleItems() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter15maxVisibleItemsEv(const QCompleter *self) {
  return self->maxVisibleItems();
}

//  void QCompleter::setMaxVisibleItems(int maxItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter18setMaxVisibleItemsEi(
    QCompleter *self,
    int maxItems) {
  self->setMaxVisibleItems(maxItems);
}

//  int QCompleter::completionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter15completionCountEv(const QCompleter *self) {
  return self->completionCount();
}

//  bool QCompleter::setCurrentRow(int row)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCompleter13setCurrentRowEi(QCompleter *self, int row) {
  return self->setCurrentRow(row);
}

//  int QCompleter::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QCompleter10currentRowEv(const QCompleter *self) {
  return self->currentRow();
}

//  QModelIndex QCompleter::currentIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK10QCompleter12currentIndexEv(const QCompleter *self) {
  return new QModelIndex(self->currentIndex());
}

//  QString QCompleter::currentCompletion() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCompleter17currentCompletionEv(
    const QCompleter *self) {
  return new QString(self->currentCompletion());
}

//  QAbstractItemModel *QCompleter::completionModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK10QCompleter15completionModelEv(
    const QCompleter *self) {
  return self->completionModel();
}

//  QString QCompleter::completionPrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCompleter16completionPrefixEv(const QCompleter *self) {
  return new QString(self->completionPrefix());
}

//  void QCompleter::setCompletionPrefix(const QString &prefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter19setCompletionPrefixERK7QString(
    QCompleter *self,
    const QString *prefix) {
  self->setCompletionPrefix(*prefix);
}

//  void QCompleter::complete(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter8completeERK5QRect(
    QCompleter *self,
    const QRect *rect) {
  self->complete(*rect);
}

//  void QCompleter::setWrapAround(bool wrap)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QCompleter13setWrapAroundEb(QCompleter *self, bool wrap) {
  self->setWrapAround(wrap);
}

//  QString QCompleter::pathFromIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QCompleter13pathFromIndexERK11QModelIndex(
    const QCompleter *self,
    const QModelIndex *index) {
  return new QString(self->pathFromIndex(*index));
}

//  QStringList QCompleter::splitPath(const QString &path) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10QCompleter9splitPathERK7QString(
    const QCompleter *self,
    const QString *path) {
  return new QList<QString>(self->splitPath(*path));
}

//  bool QCompleter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCompleter11eventFilterEP7QObjectP6QEvent(
    QCompleter *self,
    QObject *o,
    QEvent *e) {
  return self->eventFilter(o, e);
}

//  bool QCompleter::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QCompleter5eventEP6QEvent(QCompleter *self, QEvent *a0) {
  return self->event(a0);
}

//  a Python function taken by a CuteQCompleter, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCompleter(QCompleter *self, const char *key, void *call) {
  return static_cast<CuteQCompleter *>(self)->take(key, call);
}

//  QString QCompleter::pathFromIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK10QCompleter13pathFromIndexERK11QModelIndex(
    const QCompleter *self,
    const QModelIndex *index) {
  return new QString(self->QCompleter::pathFromIndex(*index));
}

//  bool QCompleter::eventFilter(QObject *o, QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QCompleter11eventFilterEP7QObjectP6QEvent(
    QCompleter *self,
    QObject *o,
    QEvent *e) {
  return static_cast<OwnQCompleter *>(self)->OwnQCompleter::eventFilter(
      o,
      e);
}

//  bool QCompleter::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QCompleter5eventEP6QEvent(QCompleter *self, QEvent *a0) {
  return static_cast<OwnQCompleter *>(self)->OwnQCompleter::event(a0);
}
