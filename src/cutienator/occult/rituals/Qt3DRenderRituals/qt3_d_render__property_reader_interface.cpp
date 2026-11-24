//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qshaderdata.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qshaderdata.h>
#include <QtCore/qvariant.h>
#include <cstring>

//  A Qt3DRender::PropertyReaderInterface that Python can take functions over in. Every Qt3DRender::PropertyReaderInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQt3DRender_PropertyReaderInterfaceCall0)(const void *, const QVariant *, int *);
class CuteQt3DRender_PropertyReaderInterface : public Qt3DRender::PropertyReaderInterface {
public:
  using Qt3DRender::PropertyReaderInterface::PropertyReaderInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender23PropertyReaderInterface12readPropertyERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QVariant Qt3DRender::PropertyReaderInterface::readProperty(const
  //      QVariant &v)
  QVariant readProperty(const QVariant &v) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_PropertyReaderInterfaceCall0 call = reinterpret_cast<CuteQt3DRender_PropertyReaderInterfaceCall0>(taken[0]);
      const QVariant * given = call(this, &v, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  Qt3DRender::PropertyReaderInterface::~PropertyReaderInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender23PropertyReaderInterfaceD1Ev(
    Qt3DRender::PropertyReaderInterface *self) {
  delete self;
}

//  QVariant Qt3DRender::PropertyReaderInterface::readProperty(const QVariant
//      &v)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN10Qt3DRender23PropertyReaderInterface12readPropertyERK8QVariant(
    Qt3DRender::PropertyReaderInterface *self,
    const QVariant *v) {
  return new QVariant(self->readProperty(*v));
}

//  a Python function taken by a CuteQt3DRender_PropertyReaderInterface, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_PropertyReaderInterface(
    Qt3DRender::PropertyReaderInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_PropertyReaderInterface *>(self)->take(key, call);
}
