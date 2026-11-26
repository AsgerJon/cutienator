//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextlist.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextlist.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTextList that Python can take functions over in. Every QTextList
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTextListCall0)(const void *, const QTextBlock *, int *);
typedef void (*CuteQTextListCall1)(const void *, const QTextBlock *, int *);
typedef void (*CuteQTextListCall2)(const void *, const QTextBlock *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextListCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTextListCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextListCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextListCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextListCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextListCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTextListCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTextList : public QTextList {
public:
  using QTextList::QTextList;
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QTextBlockGroup::blockInserted(const QTextBlock &block)
  void blockInserted(const QTextBlock &block) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextListCall0 call = reinterpret_cast<CuteQTextListCall0>(taken[0]);
      call(this, &block, &handled);
      if (handled) return;
    }
    QTextBlockGroup::blockInserted(block);
  }

  //  void QTextBlockGroup::blockRemoved(const QTextBlock &block)
  void blockRemoved(const QTextBlock &block) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextListCall1 call = reinterpret_cast<CuteQTextListCall1>(taken[1]);
      call(this, &block, &handled);
      if (handled) return;
    }
    QTextBlockGroup::blockRemoved(block);
  }

  //  void QTextBlockGroup::blockFormatChanged(const QTextBlock &block)
  void blockFormatChanged(const QTextBlock &block) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextListCall2 call = reinterpret_cast<CuteQTextListCall2>(taken[2]);
      call(this, &block, &handled);
      if (handled) return;
    }
    QTextBlockGroup::blockFormatChanged(block);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextListCall3 call = reinterpret_cast<CuteQTextListCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextListCall4 call = reinterpret_cast<CuteQTextListCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextListCall5 call = reinterpret_cast<CuteQTextListCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextListCall6 call = reinterpret_cast<CuteQTextListCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTextListCall7 call = reinterpret_cast<CuteQTextListCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTextListCall8 call = reinterpret_cast<CuteQTextListCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTextListCall9 call = reinterpret_cast<CuteQTextListCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTextList::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QTextList10metaObjectEv(
    const QTextList *self) {
  return self->metaObject();
}

//  void *QTextList::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QTextList11qt_metacastEPKc(QTextList *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTextList::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QTextList11qt_metacallEN11QMetaObject4CallEiPPv(
    QTextList *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTextList::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QTextList2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextList::tr(s, c, n));
}

//  QTextList::QTextList(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextList *ritual_ZN9QTextListC1EP13QTextDocument(QTextDocument *doc) {
  return new CuteQTextList(doc);
}

//  QTextList::~QTextList()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextListD1Ev(QTextList *self) {
  delete self;
}

//  int QTextList::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextList5countEv(const QTextList *self) {
  return self->count();
}

//  QTextBlock QTextList::item(int i) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK9QTextList4itemEi(const QTextList *self, int i) {
  return new QTextBlock(self->item(i));
}

//  int QTextList::itemNumber(const QTextBlock &a0) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QTextList10itemNumberERK10QTextBlock(
    const QTextList *self,
    const QTextBlock *a0) {
  return self->itemNumber(*a0);
}

//  QString QTextList::itemText(const QTextBlock &a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QTextList8itemTextERK10QTextBlock(
    const QTextList *self,
    const QTextBlock *a0) {
  return new QString(self->itemText(*a0));
}

//  void QTextList::removeItem(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList10removeItemEi(QTextList *self, int i) {
  self->removeItem(i);
}

//  void QTextList::remove(const QTextBlock &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList6removeERK10QTextBlock(
    QTextList *self,
    const QTextBlock *a0) {
  self->remove(*a0);
}

//  void QTextList::add(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList3addERK10QTextBlock(
    QTextList *self,
    const QTextBlock *block) {
  self->add(*block);
}

//  void QTextList::setFormat(const QTextListFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QTextList9setFormatERK15QTextListFormat(
    QTextList *self,
    const QTextListFormat *format) {
  self->setFormat(*format);
}

//  QTextListFormat QTextList::format() const
extern "C" Q_DECL_EXPORT
QTextListFormat *ritual_ZNK9QTextList6formatEv(const QTextList *self) {
  return new QTextListFormat(self->format());
}

//  QTextListPrivate *QTextList::d_func()
extern "C" Q_DECL_EXPORT
QTextListPrivate *ritual_ZN9QTextList6d_funcEv(QTextList *self) {
  return self->d_func();
}

//  const QTextListPrivate *QTextList::d_func() const
extern "C" Q_DECL_EXPORT
const QTextListPrivate *ritual_ZNK9QTextList6d_funcEv(
    const QTextList *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTextList, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextList(QTextList *self, const char *key, void *call) {
  return static_cast<CuteQTextList *>(self)->take(key, call);
}
