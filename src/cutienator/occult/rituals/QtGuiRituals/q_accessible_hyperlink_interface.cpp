//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QAccessibleHyperlinkInterface that Python can take functions over in. Every QAccessibleHyperlinkInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleHyperlinkInterfaceCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef QString * (*CuteQAccessibleHyperlinkInterfaceCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleHyperlinkInterfaceCall2)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAccessibleHyperlinkInterfaceCall3)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef bool (*CuteQAccessibleHyperlinkInterfaceCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
class CuteQAccessibleHyperlinkInterface : public QAccessibleHyperlinkInterface {
public:
  using QAccessibleHyperlinkInterface::QAccessibleHyperlinkInterface;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface6anchorEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface12anchorTargetEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface10startIndexEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface8endIndexEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK29QAccessibleHyperlinkInterface7isValidEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QString QAccessibleHyperlinkInterface::anchor() const
  QString anchor() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall0 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QString QAccessibleHyperlinkInterface::anchorTarget() const
  QString anchorTarget() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall1 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleHyperlinkInterface::startIndex() const
  int startIndex() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall2 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  int QAccessibleHyperlinkInterface::endIndex() const
  int endIndex() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall3 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  bool QAccessibleHyperlinkInterface::isValid() const
  bool isValid() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAccessibleHyperlinkInterfaceCall4 call = reinterpret_cast<CuteQAccessibleHyperlinkInterfaceCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(accessibility)
};

//  QAccessibleHyperlinkInterface::QAccessibleHyperlinkInterface()
extern "C" Q_DECL_EXPORT
QAccessibleHyperlinkInterface *ritual_ZN29QAccessibleHyperlinkInterfaceC1Ev() {
  return new CuteQAccessibleHyperlinkInterface();
}

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

#endif  // QT_CONFIG(accessibility)
