//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qexception.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#include <QtCore/qexception.h>
#include <cstring>

//  A QException that Python can take functions over in. Every QException
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
typedef void (*CuteQExceptionCall0)(const void *, int *);
#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
typedef void * (*CuteQExceptionCall1)(const void *, int *);
#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
class CuteQException : public QException {
public:
  using QException::QException;
  CuteQException(const QException & other) : QException(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK10QException5raiseEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK10QException5cloneEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
    return false;
  }

#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
  //  void QException::raise() const
  void raise() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQExceptionCall0 call = reinterpret_cast<CuteQExceptionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QException::raise();
  }
#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)

#if QT_CONFIG(future)
#if !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
  //  QException *QException::clone() const
  QException *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQExceptionCall1 call = reinterpret_cast<CuteQExceptionCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QException *>(given);
    }
    return QException::clone();
  }
#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
};

//  QException::QException()
extern "C" Q_DECL_EXPORT
QException *ritual_ZN10QExceptionC1Ev() {
  return new CuteQException();
}

//  QException::~QException()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QExceptionD1Ev(QException *self) {
  delete self;
}

//  QException::QException(const QException &a0)
extern "C" Q_DECL_EXPORT
QException *ritual_ZN10QExceptionC1ERKS_(const QException *a0) {
  return new CuteQException(*a0);
}

//  QException &QException::operator=(const QException &a0)
extern "C" Q_DECL_EXPORT
QException *ritual_ZN10QExceptionaSERKS_(
    QException *self,
    const QException *a0) {
  return &(self->operator=(*a0));
}

//  void QException::raise() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QException5raiseEv(const QException *self) {
  self->raise();
}

//  QException *QException::clone() const
extern "C" Q_DECL_EXPORT
QException *ritual_ZNK10QException5cloneEv(const QException *self) {
  return self->clone();
}

//  a Python function taken by a CuteQException, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QException(QException *self, const char *key, void *call) {
  return static_cast<CuteQException *>(self)->take(key, call);
}

//  void QException::raise() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK10QException5raiseEv(const QException *self) {
  self->QException::raise();
}

//  QException *QException::clone() const
extern "C" Q_DECL_EXPORT
QException *ritual_own_ZNK10QException5cloneEv(const QException *self) {
  return self->QException::clone();
}

#endif  // !defined(QT_NO_EXCEPTIONS) || defined(Q_QDOC)
#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
