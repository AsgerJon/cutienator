//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qundostack.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(undocommand)
#if QT_CONFIG(undocommand)
#if QT_CONFIG(undostack)
#include <QtGui/qundostack.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QUndoStack that Python can take functions over in. Every QUndoStack
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUndoStackCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUndoStackCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoStackCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoStackCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoStackCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoStackCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoStackCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQUndoStack : public QUndoStack {
public:
  using QUndoStack::QUndoStack;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQUndoStackCall0 call = reinterpret_cast<CuteQUndoStackCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQUndoStackCall1 call = reinterpret_cast<CuteQUndoStackCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQUndoStackCall2 call = reinterpret_cast<CuteQUndoStackCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQUndoStackCall3 call = reinterpret_cast<CuteQUndoStackCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQUndoStackCall4 call = reinterpret_cast<CuteQUndoStackCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQUndoStackCall5 call = reinterpret_cast<CuteQUndoStackCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQUndoStackCall6 call = reinterpret_cast<CuteQUndoStackCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QUndoStack::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QUndoStack10metaObjectEv(
    const QUndoStack *self) {
  return self->metaObject();
}

//  void *QUndoStack::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QUndoStack11qt_metacastEPKc(
    QUndoStack *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QUndoStack::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QUndoStack11qt_metacallEN11QMetaObject4CallEiPPv(
    QUndoStack *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QUndoStack::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QUndoStack2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUndoStack::tr(s, c, n));
}

//  QUndoStackPrivate *QUndoStack::d_func()
extern "C" Q_DECL_EXPORT
QUndoStackPrivate *ritual_ZN10QUndoStack6d_funcEv(QUndoStack *self) {
  return self->d_func();
}

//  const QUndoStackPrivate *QUndoStack::d_func() const
extern "C" Q_DECL_EXPORT
const QUndoStackPrivate *ritual_ZNK10QUndoStack6d_funcEv(
    const QUndoStack *self) {
  return self->d_func();
}

//  QUndoStack::QUndoStack(QObject *parent)
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZN10QUndoStackC1EP7QObject(QObject *parent) {
  return new CuteQUndoStack(parent);
}

//  QUndoStack::~QUndoStack()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStackD1Ev(QUndoStack *self) {
  delete self;
}

//  void QUndoStack::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack5clearEv(QUndoStack *self) {
  self->clear();
}

//  void QUndoStack::push(QUndoCommand *cmd)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack4pushEP12QUndoCommand(
    QUndoStack *self,
    QUndoCommand *cmd) {
  self->push(cmd);
}

//  bool QUndoStack::canUndo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack7canUndoEv(const QUndoStack *self) {
  return self->canUndo();
}

//  bool QUndoStack::canRedo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack7canRedoEv(const QUndoStack *self) {
  return self->canRedo();
}

//  QString QUndoStack::undoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoStack8undoTextEv(const QUndoStack *self) {
  return new QString(self->undoText());
}

//  QString QUndoStack::redoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoStack8redoTextEv(const QUndoStack *self) {
  return new QString(self->redoText());
}

//  int QUndoStack::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack5countEv(const QUndoStack *self) {
  return self->count();
}

//  int QUndoStack::index() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack5indexEv(const QUndoStack *self) {
  return self->index();
}

//  QString QUndoStack::text(int idx) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoStack4textEi(const QUndoStack *self, int idx) {
  return new QString(self->text(idx));
}

#if !defined(QT_NO_ACTION)
//  QAction *QUndoStack::createUndoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoStack16createUndoActionEP7QObjectRK7QString(
    const QUndoStack *self,
    QObject *parent,
    const QString *prefix) {
  return self->createUndoAction(parent, *prefix);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  QAction *QUndoStack::createRedoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoStack16createRedoActionEP7QObjectRK7QString(
    const QUndoStack *self,
    QObject *parent,
    const QString *prefix) {
  return self->createRedoAction(parent, *prefix);
}
#endif  // !defined(QT_NO_ACTION)

//  bool QUndoStack::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack8isActiveEv(const QUndoStack *self) {
  return self->isActive();
}

//  bool QUndoStack::isClean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoStack7isCleanEv(const QUndoStack *self) {
  return self->isClean();
}

//  int QUndoStack::cleanIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack10cleanIndexEv(const QUndoStack *self) {
  return self->cleanIndex();
}

//  void QUndoStack::beginMacro(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack10beginMacroERK7QString(
    QUndoStack *self,
    const QString *text) {
  self->beginMacro(*text);
}

//  void QUndoStack::endMacro()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack8endMacroEv(QUndoStack *self) {
  self->endMacro();
}

//  void QUndoStack::setUndoLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack12setUndoLimitEi(QUndoStack *self, int limit) {
  self->setUndoLimit(limit);
}

//  int QUndoStack::undoLimit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QUndoStack9undoLimitEv(const QUndoStack *self) {
  return self->undoLimit();
}

//  const QUndoCommand *QUndoStack::command(int index) const
extern "C" Q_DECL_EXPORT
const QUndoCommand *ritual_ZNK10QUndoStack7commandEi(
    const QUndoStack *self,
    int index) {
  return self->command(index);
}

//  void QUndoStack::setClean()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack8setCleanEv(QUndoStack *self) {
  self->setClean();
}

//  void QUndoStack::resetClean()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack10resetCleanEv(QUndoStack *self) {
  self->resetClean();
}

//  void QUndoStack::setIndex(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack8setIndexEi(QUndoStack *self, int idx) {
  self->setIndex(idx);
}

//  void QUndoStack::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack4undoEv(QUndoStack *self) {
  self->undo();
}

//  void QUndoStack::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack4redoEv(QUndoStack *self) {
  self->redo();
}

//  void QUndoStack::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack9setActiveEb(QUndoStack *self, bool active) {
  self->setActive(active);
}

//  void QUndoStack::indexChanged(int idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack12indexChangedEi(QUndoStack *self, int idx) {
  self->indexChanged(idx);
}

//  void QUndoStack::cleanChanged(bool clean)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack12cleanChangedEb(QUndoStack *self, bool clean) {
  self->cleanChanged(clean);
}

//  void QUndoStack::canUndoChanged(bool canUndo)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack14canUndoChangedEb(
    QUndoStack *self,
    bool canUndo) {
  self->canUndoChanged(canUndo);
}

//  void QUndoStack::canRedoChanged(bool canRedo)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack14canRedoChangedEb(
    QUndoStack *self,
    bool canRedo) {
  self->canRedoChanged(canRedo);
}

//  void QUndoStack::undoTextChanged(const QString &undoText)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack15undoTextChangedERK7QString(
    QUndoStack *self,
    const QString *undoText) {
  self->undoTextChanged(*undoText);
}

//  void QUndoStack::redoTextChanged(const QString &redoText)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoStack15redoTextChangedERK7QString(
    QUndoStack *self,
    const QString *redoText) {
  self->redoTextChanged(*redoText);
}

//  a Python function taken by a CuteQUndoStack, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUndoStack(QUndoStack *self, const char *key, void *call) {
  return static_cast<CuteQUndoStack *>(self)->take(key, call);
}

//  QList<QUndoStack *>::QList()
extern "C" Q_DECL_EXPORT
QList<QUndoStack *> *ritual_list_make_QUndoStack_ptr() {
  return new QList<QUndoStack *>();
}

//  void QList<QUndoStack *>::append(const QUndoStack * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QUndoStack_ptr(
    QList<QUndoStack *> *self,
    QUndoStack *element) {
  self->append(element);
}

//  qsizetype QList<QUndoStack *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QUndoStack_ptr(const QList<QUndoStack *> *self) {
  return self->size();
}

//  const QUndoStack * &QList<QUndoStack *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_list_at_QUndoStack_ptr(
    const QList<QUndoStack *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QUndoStack *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QUndoStack_ptr(QList<QUndoStack *> *self) {
  delete self;
}

#endif  // QT_CONFIG(undostack)
#endif  // QT_CONFIG(undocommand)
#endif  // QT_CONFIG(undocommand)
