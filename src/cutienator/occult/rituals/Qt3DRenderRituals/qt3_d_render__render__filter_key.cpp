//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/filterkey_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/filterkey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A Qt3DRender::Render::FilterKey that Python can take functions over in. Every Qt3DRender::Render::FilterKey
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_FilterKeyCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_FilterKey : public Qt3DRender::Render::FilterKey {
public:
  using Qt3DRender::Render::FilterKey::FilterKey;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::FilterKey::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_FilterKeyCall0 call = reinterpret_cast<CuteQt3DRender_Render_FilterKeyCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::FilterKey::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  const QVariant &Qt3DRender::Render::FilterKey::value() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DRender6Render9FilterKey5valueEv(
    const Qt3DRender::Render::FilterKey *self) {
  return new QVariant(self->value());
}

//  const QString &Qt3DRender::Render::FilterKey::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render9FilterKey4nameEv(
    const Qt3DRender::Render::FilterKey *self) {
  return new QString(self->name());
}

//  a Python function taken by a CuteQt3DRender_Render_FilterKey, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_FilterKey(
    Qt3DRender::Render::FilterKey *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_FilterKey *>(self)->take(key, call);
}

//  void Qt3DRender::Render::FilterKey::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render9FilterKey16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::FilterKey *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::FilterKey::syncFromFrontEnd(frontEnd, firstTime);
}
