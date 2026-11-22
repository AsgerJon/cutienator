//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QAccessibleImageInterface that Python can take functions over in. Every QAccessibleImageInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQAccessibleImageInterfaceCall0)(const void *, int *);
typedef const QSize * (*CuteQAccessibleImageInterfaceCall1)(const void *, int *);
typedef const QPoint * (*CuteQAccessibleImageInterfaceCall2)(const void *, int *);
class CuteQAccessibleImageInterface : public QAccessibleImageInterface {
public:
  using QAccessibleImageInterface::QAccessibleImageInterface;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface16imageDescriptionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface9imageSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QAccessibleImageInterface13imagePositionEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  QString QAccessibleImageInterface::imageDescription() const
  QString imageDescription() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQAccessibleImageInterfaceCall0 call = reinterpret_cast<CuteQAccessibleImageInterfaceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }

  //  QSize QAccessibleImageInterface::imageSize() const
  QSize imageSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAccessibleImageInterfaceCall1 call = reinterpret_cast<CuteQAccessibleImageInterfaceCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  QPoint QAccessibleImageInterface::imagePosition() const
  QPoint imagePosition() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAccessibleImageInterfaceCall2 call = reinterpret_cast<CuteQAccessibleImageInterfaceCall2>(taken[2]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QAccessibleImageInterface::~QAccessibleImageInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QAccessibleImageInterfaceD1Ev(
    QAccessibleImageInterface *self) {
  delete self;
}

//  QString QAccessibleImageInterface::imageDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QAccessibleImageInterface16imageDescriptionEv(
    const QAccessibleImageInterface *self) {
  return new QString(self->imageDescription());
}

//  QSize QAccessibleImageInterface::imageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK25QAccessibleImageInterface9imageSizeEv(
    const QAccessibleImageInterface *self) {
  return new QSize(self->imageSize());
}

//  QPoint QAccessibleImageInterface::imagePosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK25QAccessibleImageInterface13imagePositionEv(
    const QAccessibleImageInterface *self) {
  return new QPoint(self->imagePosition());
}

//  a Python function taken by a CuteQAccessibleImageInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAccessibleImageInterface(
    QAccessibleImageInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAccessibleImageInterface *>(self)->take(key, call);
}
