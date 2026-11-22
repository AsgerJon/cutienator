//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleHyperlinkInterface that Python can take functions over in. Every QAccessibleHyperlinkInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQAccessibleHyperlinkInterfaceCall0)(const void *, int *);
typedef int (*CuteQAccessibleHyperlinkInterfaceCall1)(const void *, int *);
typedef bool (*CuteQAccessibleHyperlinkInterfaceCall2)(const void *, int *);
class CuteQAccessibleHyperlinkInterface : public QAccessibleHyperlinkInterface {
public:
  using QAccessibleHyperlinkInterface::QAccessibleHyperlinkInterface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface10startIndexEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface8endIndexEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface7isValidEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  int QAccessibleHyperlinkInterface::startIndex() const
  int startIndex() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall0 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAccessibleHyperlinkInterface::endIndex() const
  int endIndex() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall1 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QAccessibleHyperlinkInterface::isValid() const
  bool isValid() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall2 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QAccessibleHyperlinkInterface::~QAccessibleHyperlinkInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAccessibleHyperlinkInterfaceD1Ev(
    QAccessibleHyperlinkInterface *self) {
  delete self;
}

//  QString QAccessibleHyperlinkInterface::anchor() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QAccessibleHyperlinkInterface6anchorEv(
    const QAccessibleHyperlinkInterface *self) {
  return new QString(self->anchor());
}

//  QString QAccessibleHyperlinkInterface::anchorTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK29QAccessibleHyperlinkInterface12anchorTargetEv(
    const QAccessibleHyperlinkInterface *self) {
  return new QString(self->anchorTarget());
}

//  int QAccessibleHyperlinkInterface::startIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleHyperlinkInterface10startIndexEv(
    const QAccessibleHyperlinkInterface *self) {
  return self->startIndex();
}

//  int QAccessibleHyperlinkInterface::endIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QAccessibleHyperlinkInterface8endIndexEv(
    const QAccessibleHyperlinkInterface *self) {
  return self->endIndex();
}

//  bool QAccessibleHyperlinkInterface::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QAccessibleHyperlinkInterface7isValidEv(
    const QAccessibleHyperlinkInterface *self) {
  return self->isValid();
}

//  a Python function taken by a CuteQAccessibleHyperlinkInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleHyperlinkInterface(
    QAccessibleHyperlinkInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleHyperlinkInterface *>(self)->take(key, call);
}
