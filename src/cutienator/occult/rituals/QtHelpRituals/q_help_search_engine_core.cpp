//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpsearchenginecore.h, Qt 6.12.0. Changes made here are lost.
#include <QtHelp/qhelpsearchenginecore.h>
#include <QtCore/qstring.h>
#include <QtHelp/qhelpsearchresult.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QHelpSearchEngineCore that Python can take functions over in. Every QHelpSearchEngineCore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchEngineCoreCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchEngineCoreCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCoreCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCoreCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCoreCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCoreCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCoreCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpSearchEngineCore : public QHelpSearchEngineCore {
public:
  using QHelpSearchEngineCore::QHelpSearchEngineCore;
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
      CuteQHelpSearchEngineCoreCall0 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall0>(taken[0]);
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
      CuteQHelpSearchEngineCoreCall1 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall1>(taken[1]);
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
      CuteQHelpSearchEngineCoreCall2 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall2>(taken[2]);
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
      CuteQHelpSearchEngineCoreCall3 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall3>(taken[3]);
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
      CuteQHelpSearchEngineCoreCall4 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall4>(taken[4]);
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
      CuteQHelpSearchEngineCoreCall5 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall5>(taken[5]);
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
      CuteQHelpSearchEngineCoreCall6 call = reinterpret_cast<CuteQHelpSearchEngineCoreCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpSearchEngineCore::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QHelpSearchEngineCore10metaObjectEv(
    const QHelpSearchEngineCore *self) {
  return self->metaObject();
}

//  QString QHelpSearchEngineCore::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QHelpSearchEngineCore2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpSearchEngineCore::tr(s, c, n));
}

//  QHelpSearchEngineCore::QHelpSearchEngineCore(QHelpEngineCore *helpEngine,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QHelpSearchEngineCore *ritual_ZN21QHelpSearchEngineCoreC1EP15QHelpEngineCoreP7QObject(
    QHelpEngineCore *helpEngine,
    QObject *parent) {
  return new CuteQHelpSearchEngineCore(helpEngine, parent);
}

//  QHelpSearchEngineCore::~QHelpSearchEngineCore()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHelpSearchEngineCoreD1Ev(QHelpSearchEngineCore *self) {
  delete self;
}

//  int QHelpSearchEngineCore::searchResultCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QHelpSearchEngineCore17searchResultCountEv(
    const QHelpSearchEngineCore *self) {
  return self->searchResultCount();
}

//  QList<QHelpSearchResult> QHelpSearchEngineCore::searchResults(int start,
//      int end) const
extern "C" Q_DECL_EXPORT
QList<QHelpSearchResult> *ritual_ZNK21QHelpSearchEngineCore13searchResultsEii(
    const QHelpSearchEngineCore *self,
    int start,
    int end) {
  return new QList<QHelpSearchResult>(self->searchResults(start, end));
}

//  QString QHelpSearchEngineCore::searchInput() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QHelpSearchEngineCore11searchInputEv(
    const QHelpSearchEngineCore *self) {
  return new QString(self->searchInput());
}

//  void QHelpSearchEngineCore::reindexDocumentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHelpSearchEngineCore20reindexDocumentationEv(
    QHelpSearchEngineCore *self) {
  self->reindexDocumentation();
}

//  void QHelpSearchEngineCore::cancelIndexing()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHelpSearchEngineCore14cancelIndexingEv(
    QHelpSearchEngineCore *self) {
  self->cancelIndexing();
}

//  void QHelpSearchEngineCore::search(const QString &searchInput)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHelpSearchEngineCore6searchERK7QString(
    QHelpSearchEngineCore *self,
    const QString *searchInput) {
  self->search(*searchInput);
}

//  void QHelpSearchEngineCore::cancelSearching()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHelpSearchEngineCore15cancelSearchingEv(
    QHelpSearchEngineCore *self) {
  self->cancelSearching();
}

//  void QHelpSearchEngineCore::scheduleIndexDocumentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHelpSearchEngineCore26scheduleIndexDocumentationEv(
    QHelpSearchEngineCore *self) {
  self->scheduleIndexDocumentation();
}

//  a Python function taken by a CuteQHelpSearchEngineCore, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpSearchEngineCore(
    QHelpSearchEngineCore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpSearchEngineCore *>(self)->take(key, call);
}
