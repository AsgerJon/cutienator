//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpsearchengine.h, Qt 6.12.0. Edited by hand on 2026-11-25:
//  the config header of QtTools is included before the first #if,
//  as QT_CONFIG(fullqthelp) is defined there. Kept as it is when
//  the generator runs again.
#include <QtHelp/qhelp_global.h>
#include <QtTools/qttools-config.h>
#if QT_CONFIG(fullqthelp)
#include <QtHelp/QtHelp>
#include <QtHelp/qhelpsearchengine.h>
#include <QtCore/qstring.h>
#include <QtHelp/qhelpsearchresult.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QHelpSearchEngine that Python can take functions over in. Every QHelpSearchEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpSearchEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpSearchEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpSearchEngine : public QHelpSearchEngine {
public:
  using QHelpSearchEngine::QHelpSearchEngine;
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
      CuteQHelpSearchEngineCall0 call = reinterpret_cast<CuteQHelpSearchEngineCall0>(taken[0]);
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
      CuteQHelpSearchEngineCall1 call = reinterpret_cast<CuteQHelpSearchEngineCall1>(taken[1]);
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
      CuteQHelpSearchEngineCall2 call = reinterpret_cast<CuteQHelpSearchEngineCall2>(taken[2]);
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
      CuteQHelpSearchEngineCall3 call = reinterpret_cast<CuteQHelpSearchEngineCall3>(taken[3]);
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
      CuteQHelpSearchEngineCall4 call = reinterpret_cast<CuteQHelpSearchEngineCall4>(taken[4]);
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
      CuteQHelpSearchEngineCall5 call = reinterpret_cast<CuteQHelpSearchEngineCall5>(taken[5]);
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
      CuteQHelpSearchEngineCall6 call = reinterpret_cast<CuteQHelpSearchEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpSearchEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QHelpSearchEngine10metaObjectEv(
    const QHelpSearchEngine *self) {
  return self->metaObject();
}

//  void *QHelpSearchEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QHelpSearchEngine11qt_metacastEPKc(
    QHelpSearchEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QHelpSearchEngine::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QHelpSearchEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpSearchEngine::tr(s, c, n));
}

//  QHelpSearchEngine::QHelpSearchEngine(QHelpEngineCore *helpEngine, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QHelpSearchEngine *ritual_ZN17QHelpSearchEngineC1EP15QHelpEngineCoreP7QObject(
    QHelpEngineCore *helpEngine,
    QObject *parent) {
  return new CuteQHelpSearchEngine(helpEngine, parent);
}

//  QHelpSearchEngine::~QHelpSearchEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngineD1Ev(QHelpSearchEngine *self) {
  delete self;
}

//  QHelpSearchQueryWidget *QHelpSearchEngine::queryWidget()
extern "C" Q_DECL_EXPORT
QHelpSearchQueryWidget *ritual_ZN17QHelpSearchEngine11queryWidgetEv(
    QHelpSearchEngine *self) {
  return self->queryWidget();
}

//  QHelpSearchResultWidget *QHelpSearchEngine::resultWidget()
extern "C" Q_DECL_EXPORT
QHelpSearchResultWidget *ritual_ZN17QHelpSearchEngine12resultWidgetEv(
    QHelpSearchEngine *self) {
  return self->resultWidget();
}

#if QT_DEPRECATED_SINCE(5, 9)
//  int QHelpSearchEngine::hitsCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHelpSearchEngine9hitsCountEv(
    const QHelpSearchEngine *self) {
  return self->hitsCount();
}
#endif  // QT_DEPRECATED_SINCE(5, 9)

#if QT_DEPRECATED_SINCE(5, 9)
//  int QHelpSearchEngine::hitCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHelpSearchEngine8hitCountEv(const QHelpSearchEngine *self) {
  return self->hitCount();
}
#endif  // QT_DEPRECATED_SINCE(5, 9)

#if QT_DEPRECATED_SINCE(5, 9)
//  QList<QHelpSearchQuery> QHelpSearchEngine::query() const
extern "C" Q_DECL_EXPORT
QList<QHelpSearchQuery> *ritual_ZNK17QHelpSearchEngine5queryEv(
    const QHelpSearchEngine *self) {
  return new QList<QHelpSearchQuery>(self->query());
}
#endif  // QT_DEPRECATED_SINCE(5, 9)

//  int QHelpSearchEngine::searchResultCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QHelpSearchEngine17searchResultCountEv(
    const QHelpSearchEngine *self) {
  return self->searchResultCount();
}

//  QList<QHelpSearchResult> QHelpSearchEngine::searchResults(int start, int
//      end) const
extern "C" Q_DECL_EXPORT
QList<QHelpSearchResult> *ritual_ZNK17QHelpSearchEngine13searchResultsEii(
    const QHelpSearchEngine *self,
    int start,
    int end) {
  return new QList<QHelpSearchResult>(self->searchResults(start, end));
}

//  QString QHelpSearchEngine::searchInput() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QHelpSearchEngine11searchInputEv(
    const QHelpSearchEngine *self) {
  return new QString(self->searchInput());
}

//  void QHelpSearchEngine::reindexDocumentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine20reindexDocumentationEv(
    QHelpSearchEngine *self) {
  self->reindexDocumentation();
}

//  void QHelpSearchEngine::cancelIndexing()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine14cancelIndexingEv(
    QHelpSearchEngine *self) {
  self->cancelIndexing();
}

#if QT_DEPRECATED_SINCE(5, 9)
//  void QHelpSearchEngine::search(const QList<QHelpSearchQuery> &queryList)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine6searchERK5QListI16QHelpSearchQueryE(
    QHelpSearchEngine *self,
    const QList<QHelpSearchQuery> *queryList) {
  self->search(*queryList);
}
#endif  // QT_DEPRECATED_SINCE(5, 9)

//  void QHelpSearchEngine::search(const QString &searchInput)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine6searchERK7QString(
    QHelpSearchEngine *self,
    const QString *searchInput) {
  self->search(*searchInput);
}

//  void QHelpSearchEngine::cancelSearching()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine15cancelSearchingEv(
    QHelpSearchEngine *self) {
  self->cancelSearching();
}

//  void QHelpSearchEngine::scheduleIndexDocumentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine26scheduleIndexDocumentationEv(
    QHelpSearchEngine *self) {
  self->scheduleIndexDocumentation();
}

//  void QHelpSearchEngine::indexingStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine15indexingStartedEv(
    QHelpSearchEngine *self) {
  self->indexingStarted();
}

//  void QHelpSearchEngine::indexingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine16indexingFinishedEv(
    QHelpSearchEngine *self) {
  self->indexingFinished();
}

//  void QHelpSearchEngine::searchingStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine16searchingStartedEv(
    QHelpSearchEngine *self) {
  self->searchingStarted();
}

//  void QHelpSearchEngine::searchingFinished(int searchResultCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine17searchingFinishedEi(
    QHelpSearchEngine *self,
    int searchResultCount) {
  self->searchingFinished(searchResultCount);
}

//  void QHelpSearchEngine::indexDocumentation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QHelpSearchEngine18indexDocumentationEv(
    QHelpSearchEngine *self) {
  self->indexDocumentation();
}

//  a Python function taken by a CuteQHelpSearchEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpSearchEngine(
    QHelpSearchEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpSearchEngine *>(self)->take(key, call);
}

#endif  // QT_CONFIG(fullqthelp)
