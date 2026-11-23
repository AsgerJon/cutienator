//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QTextBlockGroup may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTextBlockGroup : QTextBlockGroup {
  using QTextBlockGroup::blockInserted;
  using QTextBlockGroup::blockRemoved;
  using QTextBlockGroup::blockFormatChanged;
};

//  A QTextBlockGroup that Python can take functions over in. Every QTextBlockGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTextBlockGroupCall0)(const void *, const QTextBlock *, int *);
typedef void (*CuteQTextBlockGroupCall1)(const void *, const QTextBlock *, int *);
typedef void (*CuteQTextBlockGroupCall2)(const void *, const QTextBlock *, int *);
typedef bool (*CuteQTextBlockGroupCall3)(const void *, QEvent *, int *);
typedef bool (*CuteQTextBlockGroupCall4)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTextBlockGroupCall5)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTextBlockGroupCall6)(const void *, QChildEvent *, int *);
typedef void (*CuteQTextBlockGroupCall7)(const void *, QEvent *, int *);
typedef void (*CuteQTextBlockGroupCall8)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTextBlockGroupCall9)(const void *, const QMetaMethod *, int *);
class CuteQTextBlockGroup : public QTextBlockGroup {
public:
  using QTextBlockGroup::QTextBlockGroup;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QTextBlockGroup13blockInsertedERK10QTextBlock")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QTextBlockGroup12blockRemovedERK10QTextBlock")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QTextBlockGroup18blockFormatChangedERK10QTextBlock")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QTextBlockGroup::blockInserted(const QTextBlock &block)
  void blockInserted(const QTextBlock &block) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextBlockGroupCall0 call = reinterpret_cast<CuteQTextBlockGroupCall0>(taken[0]);
      call(this, &block, &handled);
      if (handled) return;
    }
    QTextBlockGroup::blockInserted(block);
  }

  //  void QTextBlockGroup::blockRemoved(const QTextBlock &block)
  void blockRemoved(const QTextBlock &block) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextBlockGroupCall1 call = reinterpret_cast<CuteQTextBlockGroupCall1>(taken[1]);
      call(this, &block, &handled);
      if (handled) return;
    }
    QTextBlockGroup::blockRemoved(block);
  }

  //  void QTextBlockGroup::blockFormatChanged(const QTextBlock &block)
  void blockFormatChanged(const QTextBlock &block) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextBlockGroupCall2 call = reinterpret_cast<CuteQTextBlockGroupCall2>(taken[2]);
      call(this, &block, &handled);
      if (handled) return;
    }
    QTextBlockGroup::blockFormatChanged(block);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextBlockGroupCall3 call = reinterpret_cast<CuteQTextBlockGroupCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextBlockGroupCall4 call = reinterpret_cast<CuteQTextBlockGroupCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextBlockGroupCall5 call = reinterpret_cast<CuteQTextBlockGroupCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextBlockGroupCall6 call = reinterpret_cast<CuteQTextBlockGroupCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextBlockGroupCall7 call = reinterpret_cast<CuteQTextBlockGroupCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextBlockGroupCall8 call = reinterpret_cast<CuteQTextBlockGroupCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextBlockGroupCall9 call = reinterpret_cast<CuteQTextBlockGroupCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTextBlockGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QTextBlockGroup10metaObjectEv(
    const QTextBlockGroup *self) {
  return self->metaObject();
}

//  QString QTextBlockGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QTextBlockGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextBlockGroup::tr(s, c, n));
}

//  QTextBlockGroup::QTextBlockGroup(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextBlockGroup *ritual_ZN15QTextBlockGroupC1EP13QTextDocument(
    QTextDocument *doc) {
  return new CuteQTextBlockGroup(doc);
}

//  QTextBlockGroup::~QTextBlockGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextBlockGroupD1Ev(QTextBlockGroup *self) {
  delete self;
}

//  void QTextBlockGroup::blockInserted(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextBlockGroup13blockInsertedERK10QTextBlock(
    QTextBlockGroup *self,
    const QTextBlock *block) {
  self->blockInserted(*block);
}

//  void QTextBlockGroup::blockRemoved(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextBlockGroup12blockRemovedERK10QTextBlock(
    QTextBlockGroup *self,
    const QTextBlock *block) {
  self->blockRemoved(*block);
}

//  void QTextBlockGroup::blockFormatChanged(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextBlockGroup18blockFormatChangedERK10QTextBlock(
    QTextBlockGroup *self,
    const QTextBlock *block) {
  self->blockFormatChanged(*block);
}

//  QList<QTextBlock> QTextBlockGroup::blockList() const
extern "C" Q_DECL_EXPORT
QList<QTextBlock> *ritual_ZNK15QTextBlockGroup9blockListEv(
    const QTextBlockGroup *self) {
  return new QList<QTextBlock>(self->blockList());
}

//  a Python function taken by a CuteQTextBlockGroup, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextBlockGroup(
    QTextBlockGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTextBlockGroup *>(self)->take(key, call);
}

//  void QTextBlockGroup::blockInserted(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QTextBlockGroup13blockInsertedERK10QTextBlock(
    QTextBlockGroup *self,
    const QTextBlock *block) {
  static_cast<OwnQTextBlockGroup *>(self)->OwnQTextBlockGroup::blockInserted(
      *block);
}

//  void QTextBlockGroup::blockRemoved(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QTextBlockGroup12blockRemovedERK10QTextBlock(
    QTextBlockGroup *self,
    const QTextBlock *block) {
  static_cast<OwnQTextBlockGroup *>(self)->OwnQTextBlockGroup::blockRemoved(
      *block);
}

//  void QTextBlockGroup::blockFormatChanged(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QTextBlockGroup18blockFormatChangedERK10QTextBlock(
    QTextBlockGroup *self,
    const QTextBlock *block) {
  static_cast<OwnQTextBlockGroup *>(self)->OwnQTextBlockGroup::blockFormatChanged(
      *block);
}
