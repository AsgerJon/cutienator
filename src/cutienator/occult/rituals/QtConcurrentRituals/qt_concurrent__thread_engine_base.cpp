//  Written by dev_tooling.RitualGenerator from the records of
//  QtConcurrent/qtconcurrentthreadengine.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtConcurrent/qtconcurrent_global.h>
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#include <QtConcurrent/qtconcurrentthreadengine.h>
#include <cstring>

//  Only a class built on QtConcurrent::ThreadEngineBase may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQtConcurrent_ThreadEngineBase : QtConcurrent::ThreadEngineBase {
  using QtConcurrent::ThreadEngineBase::start;
  using QtConcurrent::ThreadEngineBase::finish;
  using QtConcurrent::ThreadEngineBase::threadFunction;
  using QtConcurrent::ThreadEngineBase::shouldStartThread;
  using QtConcurrent::ThreadEngineBase::shouldThrottleThread;
};

//  A QtConcurrent::ThreadEngineBase that Python can take functions over in. Every QtConcurrent::ThreadEngineBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef void (*CuteQtConcurrent_ThreadEngineBaseCall0)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef void (*CuteQtConcurrent_ThreadEngineBaseCall1)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef int (*CuteQtConcurrent_ThreadEngineBaseCall2)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef bool (*CuteQtConcurrent_ThreadEngineBaseCall3)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef bool (*CuteQtConcurrent_ThreadEngineBaseCall4)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef void (*CuteQtConcurrent_ThreadEngineBaseCall5)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
typedef void (*CuteQtConcurrent_ThreadEngineBaseCall6)(const void *, int *);
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
class CuteQtConcurrent_ThreadEngineBase : public QtConcurrent::ThreadEngineBase {
public:
  using QtConcurrent::ThreadEngineBase::ThreadEngineBase;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN12QtConcurrent16ThreadEngineBase5startEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN12QtConcurrent16ThreadEngineBase6finishEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN12QtConcurrent16ThreadEngineBase14threadFunctionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN12QtConcurrent16ThreadEngineBase17shouldStartThreadEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN12QtConcurrent16ThreadEngineBase20shouldThrottleThreadEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN12QtConcurrent16ThreadEngineBase18asynchronousFinishEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
    return false;
  }

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  void QtConcurrent::ThreadEngineBase::start()
  void start() override {
    if (taken[0]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall0 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QtConcurrent::ThreadEngineBase::start();
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  void QtConcurrent::ThreadEngineBase::finish()
  void finish() override {
    if (taken[1]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall1 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QtConcurrent::ThreadEngineBase::finish();
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  ThreadFunctionResult QtConcurrent::ThreadEngineBase::threadFunction()
  QtConcurrent::ThreadFunctionResult threadFunction() override {
    if (taken[2]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall2 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QtConcurrent::ThreadFunctionResult>(given);
    }
    return QtConcurrent::ThreadEngineBase::threadFunction();
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  bool QtConcurrent::ThreadEngineBase::shouldStartThread()
  bool shouldStartThread() override {
    if (taken[3]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall3 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtConcurrent::ThreadEngineBase::shouldStartThread();
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  bool QtConcurrent::ThreadEngineBase::shouldThrottleThread()
  bool shouldThrottleThread() override {
    if (taken[4]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall4 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QtConcurrent::ThreadEngineBase::shouldThrottleThread();
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  void QtConcurrent::ThreadEngineBase::run()
  void run() override {
    if (taken[5]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall5 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QtConcurrent::ThreadEngineBase::run();
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)

#if !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
  //  void QtConcurrent::ThreadEngineBase::asynchronousFinish()
  void asynchronousFinish() override {
    if (taken[6]) {
      int handled = 0;
      CuteQtConcurrent_ThreadEngineBaseCall6 call = reinterpret_cast<CuteQtConcurrent_ThreadEngineBaseCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
};

//  QtConcurrent::ThreadEngineBase::~ThreadEngineBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent16ThreadEngineBaseD1Ev(
    QtConcurrent::ThreadEngineBase *self) {
  delete self;
}

//  void QtConcurrent::ThreadEngineBase::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent16ThreadEngineBase5startEv(
    QtConcurrent::ThreadEngineBase *self) {
  self->start();
}

//  void QtConcurrent::ThreadEngineBase::finish()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent16ThreadEngineBase6finishEv(
    QtConcurrent::ThreadEngineBase *self) {
  self->finish();
}

//  ThreadFunctionResult QtConcurrent::ThreadEngineBase::threadFunction()
extern "C" Q_DECL_EXPORT
QtConcurrent::ThreadFunctionResult ritual_ZN12QtConcurrent16ThreadEngineBase14threadFunctionEv(
    QtConcurrent::ThreadEngineBase *self) {
  return self->threadFunction();
}

//  bool QtConcurrent::ThreadEngineBase::shouldStartThread()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QtConcurrent16ThreadEngineBase17shouldStartThreadEv(
    QtConcurrent::ThreadEngineBase *self) {
  return self->shouldStartThread();
}

//  bool QtConcurrent::ThreadEngineBase::shouldThrottleThread()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QtConcurrent16ThreadEngineBase20shouldThrottleThreadEv(
    QtConcurrent::ThreadEngineBase *self) {
  return self->shouldThrottleThread();
}

//  void QtConcurrent::ThreadEngineBase::asynchronousFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtConcurrent16ThreadEngineBase18asynchronousFinishEv(
    QtConcurrent::ThreadEngineBase *self) {
  self->asynchronousFinish();
}

//  a Python function taken by a CuteQtConcurrent_ThreadEngineBase, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QtConcurrent_ThreadEngineBase(
    QtConcurrent::ThreadEngineBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQtConcurrent_ThreadEngineBase *>(self)->take(key, call);
}

//  void QtConcurrent::ThreadEngineBase::start()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QtConcurrent16ThreadEngineBase5startEv(
    QtConcurrent::ThreadEngineBase *self) {
  static_cast<OwnQtConcurrent_ThreadEngineBase *>(self)->OwnQtConcurrent_ThreadEngineBase::start();
}

//  void QtConcurrent::ThreadEngineBase::finish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QtConcurrent16ThreadEngineBase6finishEv(
    QtConcurrent::ThreadEngineBase *self) {
  static_cast<OwnQtConcurrent_ThreadEngineBase *>(self)->OwnQtConcurrent_ThreadEngineBase::finish();
}

//  ThreadFunctionResult QtConcurrent::ThreadEngineBase::threadFunction()
extern "C" Q_DECL_EXPORT
QtConcurrent::ThreadFunctionResult ritual_own_ZN12QtConcurrent16ThreadEngineBase14threadFunctionEv(
    QtConcurrent::ThreadEngineBase *self) {
  return static_cast<OwnQtConcurrent_ThreadEngineBase *>(self)->OwnQtConcurrent_ThreadEngineBase::threadFunction();
}

//  bool QtConcurrent::ThreadEngineBase::shouldStartThread()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QtConcurrent16ThreadEngineBase17shouldStartThreadEv(
    QtConcurrent::ThreadEngineBase *self) {
  return static_cast<OwnQtConcurrent_ThreadEngineBase *>(self)->OwnQtConcurrent_ThreadEngineBase::shouldStartThread();
}

//  bool QtConcurrent::ThreadEngineBase::shouldThrottleThread()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QtConcurrent16ThreadEngineBase20shouldThrottleThreadEv(
    QtConcurrent::ThreadEngineBase *self) {
  return static_cast<OwnQtConcurrent_ThreadEngineBase *>(self)->OwnQtConcurrent_ThreadEngineBase::shouldThrottleThread();
}

//  void QtConcurrent::ThreadEngineBase::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QtConcurrent16ThreadEngineBase3runEv(
    QtConcurrent::ThreadEngineBase *self) {
  self->QtConcurrent::ThreadEngineBase::run();
}

#endif  // !defined(QT_NO_CONCURRENT) ||defined(Q_QDOC)
