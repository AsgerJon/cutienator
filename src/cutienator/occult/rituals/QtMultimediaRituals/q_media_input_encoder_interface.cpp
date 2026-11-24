//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qmediainputencoderinterface_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qmediainputencoderinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMediaInputEncoderInterface that Python can take functions over in. Every QMediaInputEncoderInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQMediaInputEncoderInterfaceCall0)(const void *, int *);
class CuteQMediaInputEncoderInterface : public QMediaInputEncoderInterface {
public:
  using QMediaInputEncoderInterface::QMediaInputEncoderInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK27QMediaInputEncoderInterface12canPushFrameEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool QMediaInputEncoderInterface::canPushFrame() const
  bool canPushFrame() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMediaInputEncoderInterfaceCall0 call = reinterpret_cast<CuteQMediaInputEncoderInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QMediaInputEncoderInterface::~QMediaInputEncoderInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMediaInputEncoderInterfaceD1Ev(
    QMediaInputEncoderInterface *self) {
  delete self;
}

//  bool QMediaInputEncoderInterface::canPushFrame() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QMediaInputEncoderInterface12canPushFrameEv(
    const QMediaInputEncoderInterface *self) {
  return self->canPushFrame();
}

//  a Python function taken by a CuteQMediaInputEncoderInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMediaInputEncoderInterface(
    QMediaInputEncoderInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMediaInputEncoderInterface *>(self)->take(key, call);
}
