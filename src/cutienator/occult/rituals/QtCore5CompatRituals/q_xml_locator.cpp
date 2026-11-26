//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore5Compat/qxml.h>
#include <cstring>

//  A QXmlLocator that Python can take functions over in. Every QXmlLocator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQXmlLocatorCall0)(const void *, int *);
typedef int (*CuteQXmlLocatorCall1)(const void *, int *);
class CuteQXmlLocator : public QXmlLocator {
public:
  using QXmlLocator::QXmlLocator;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QXmlLocator12columnNumberEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QXmlLocator10lineNumberEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  int QXmlLocator::columnNumber() const
  int columnNumber() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQXmlLocatorCall0 call = reinterpret_cast<CuteQXmlLocatorCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QXmlLocator::lineNumber() const
  int lineNumber() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQXmlLocatorCall1 call = reinterpret_cast<CuteQXmlLocatorCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QXmlLocator::QXmlLocator()
extern "C" Q_DECL_EXPORT
QXmlLocator *ritual_ZN11QXmlLocatorC1Ev() {
  return new CuteQXmlLocator();
}

//  QXmlLocator::~QXmlLocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QXmlLocatorD1Ev(QXmlLocator *self) {
  delete self;
}

//  int QXmlLocator::columnNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QXmlLocator12columnNumberEv(const QXmlLocator *self) {
  return self->columnNumber();
}

//  int QXmlLocator::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QXmlLocator10lineNumberEv(const QXmlLocator *self) {
  return self->lineNumber();
}

//  a Python function taken by a CuteQXmlLocator, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QXmlLocator(
    QXmlLocator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQXmlLocator *>(self)->take(key, call);
}
