//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qundogroup.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(undogroup)
#include <QtGui/qundogroup.h>
#include <QtCore/qstring.h>
#include <QtGui/qundostack.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QUndoGroup that Python can take functions over in. Every QUndoGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUndoGroupCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQUndoGroupCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoGroupCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoGroupCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoGroupCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoGroupCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQUndoGroupCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQUndoGroup : public QUndoGroup {
public:
  using QUndoGroup::QUndoGroup;
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
      CuteQUndoGroupCall0 call = reinterpret_cast<CuteQUndoGroupCall0>(taken[0]);
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
      CuteQUndoGroupCall1 call = reinterpret_cast<CuteQUndoGroupCall1>(taken[1]);
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
      CuteQUndoGroupCall2 call = reinterpret_cast<CuteQUndoGroupCall2>(taken[2]);
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
      CuteQUndoGroupCall3 call = reinterpret_cast<CuteQUndoGroupCall3>(taken[3]);
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
      CuteQUndoGroupCall4 call = reinterpret_cast<CuteQUndoGroupCall4>(taken[4]);
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
      CuteQUndoGroupCall5 call = reinterpret_cast<CuteQUndoGroupCall5>(taken[5]);
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
      CuteQUndoGroupCall6 call = reinterpret_cast<CuteQUndoGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QUndoGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QUndoGroup10metaObjectEv(
    const QUndoGroup *self) {
  return self->metaObject();
}

//  QString QUndoGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QUndoGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUndoGroup::tr(s, c, n));
}

//  QUndoGroup::QUndoGroup(QObject *parent)
extern "C" Q_DECL_EXPORT
QUndoGroup *ritual_ZN10QUndoGroupC1EP7QObject(QObject *parent) {
  return new CuteQUndoGroup(parent);
}

//  QUndoGroup::~QUndoGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroupD1Ev(QUndoGroup *self) {
  delete self;
}

//  void QUndoGroup::addStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup8addStackEP10QUndoStack(
    QUndoGroup *self,
    QUndoStack *stack) {
  self->addStack(stack);
}

//  void QUndoGroup::removeStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup11removeStackEP10QUndoStack(
    QUndoGroup *self,
    QUndoStack *stack) {
  self->removeStack(stack);
}

//  QList<QUndoStack *> QUndoGroup::stacks() const
extern "C" Q_DECL_EXPORT
QList<QUndoStack *> *ritual_ZNK10QUndoGroup6stacksEv(
    const QUndoGroup *self) {
  return new QList<QUndoStack *>(self->stacks());
}

//  QUndoStack *QUndoGroup::activeStack() const
extern "C" Q_DECL_EXPORT
QUndoStack *ritual_ZNK10QUndoGroup11activeStackEv(const QUndoGroup *self) {
  return self->activeStack();
}

#if !defined(QT_NO_ACTION)
//  QAction *QUndoGroup::createUndoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoGroup16createUndoActionEP7QObjectRK7QString(
    const QUndoGroup *self,
    QObject *parent,
    const QString *prefix) {
  return self->createUndoAction(parent, *prefix);
}
#endif  // !defined(QT_NO_ACTION)

#if !defined(QT_NO_ACTION)
//  QAction *QUndoGroup::createRedoAction(QObject *parent, const QString
//      &prefix) const
extern "C" Q_DECL_EXPORT
QAction *ritual_ZNK10QUndoGroup16createRedoActionEP7QObjectRK7QString(
    const QUndoGroup *self,
    QObject *parent,
    const QString *prefix) {
  return self->createRedoAction(parent, *prefix);
}
#endif  // !defined(QT_NO_ACTION)

//  bool QUndoGroup::canUndo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoGroup7canUndoEv(const QUndoGroup *self) {
  return self->canUndo();
}

//  bool QUndoGroup::canRedo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoGroup7canRedoEv(const QUndoGroup *self) {
  return self->canRedo();
}

//  QString QUndoGroup::undoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoGroup8undoTextEv(const QUndoGroup *self) {
  return new QString(self->undoText());
}

//  QString QUndoGroup::redoText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QUndoGroup8redoTextEv(const QUndoGroup *self) {
  return new QString(self->redoText());
}

//  bool QUndoGroup::isClean() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QUndoGroup7isCleanEv(const QUndoGroup *self) {
  return self->isClean();
}

//  void QUndoGroup::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup4undoEv(QUndoGroup *self) {
  self->undo();
}

//  void QUndoGroup::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup4redoEv(QUndoGroup *self) {
  self->redo();
}

//  void QUndoGroup::setActiveStack(QUndoStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QUndoGroup14setActiveStackEP10QUndoStack(
    QUndoGroup *self,
    QUndoStack *stack) {
  self->setActiveStack(stack);
}

//  a Python function taken by a CuteQUndoGroup, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUndoGroup(QUndoGroup *self, const char *key, void *call) {
  return static_cast<CuteQUndoGroup *>(self)->take(key, call);
}

#endif  // QT_CONFIG(undogroup)
