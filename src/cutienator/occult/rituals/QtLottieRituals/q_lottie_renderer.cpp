//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottierenderer_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: included QtGui/qtransform.h before the
//  private header, whose line 91 uses QTransform without including it. Kept
//  as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#include <QtGui/qtransform.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottierenderer_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieprecomposition_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottielayer_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottietextlayer_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiegroup_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottierect_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieellipse_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiepolystar_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieround_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiefill_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiegfill_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieimage_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiestroke_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiebasictransform_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieshapetransform_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiefreeformshape_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottietrimpath_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiefilleffect_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottierepeater_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottiebase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QLottieRenderer that Python can take functions over in. Every QLottieRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLottieRendererCall0)(const void *, int *);
typedef void (*CuteQLottieRendererCall1)(const void *, int *);
typedef void (*CuteQLottieRendererCall2)(const void *, int, int *);
typedef int (*CuteQLottieRendererCall3)(const void *, int *);
typedef void (*CuteQLottieRendererCall4)(const void *, const QLottiePrecomposition *, int *);
typedef void (*CuteQLottieRendererCall5)(const void *, const QLottieLayer *, int *);
typedef void (*CuteQLottieRendererCall6)(const void *, const QLottieSolidLayer *, int *);
typedef void (*CuteQLottieRendererCall7)(const void *, const QLottieTextLayer *, int *);
typedef void (*CuteQLottieRendererCall8)(const void *, const QLottieGroup *, int *);
typedef void (*CuteQLottieRendererCall9)(const void *, const QLottieRect *, int *);
typedef void (*CuteQLottieRendererCall10)(const void *, const QLottieEllipse *, int *);
typedef void (*CuteQLottieRendererCall11)(const void *, const QLottiePolyStar *, int *);
typedef void (*CuteQLottieRendererCall12)(const void *, const QLottieRound *, int *);
typedef void (*CuteQLottieRendererCall13)(const void *, const QLottieFill *, int *);
typedef void (*CuteQLottieRendererCall14)(const void *, const QLottieGFill *, int *);
typedef void (*CuteQLottieRendererCall15)(const void *, const QLottieImage *, int *);
typedef void (*CuteQLottieRendererCall16)(const void *, const QLottieStroke *, int *);
typedef void (*CuteQLottieRendererCall17)(const void *, const QLottieBasicTransform *, int *);
typedef void (*CuteQLottieRendererCall18)(const void *, const QLottieShapeTransform *, int *);
typedef void (*CuteQLottieRendererCall19)(const void *, const QLottieFreeFormShape *, int *);
typedef void (*CuteQLottieRendererCall20)(const void *, const QLottieTrimPath *, int *);
typedef void (*CuteQLottieRendererCall21)(const void *, const QLottieFillEffect *, int *);
typedef void (*CuteQLottieRendererCall22)(const void *, const QLottieRepeater *, int *);
typedef void (*CuteQLottieRendererCall23)(const void *, const QLottieLayer *, int *);
typedef void (*CuteQLottieRendererCall24)(const void *, const QLottieGroup *, int *);
class CuteQLottieRenderer : public QLottieRenderer {
public:
  using QLottieRenderer::QLottieRenderer;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN15QLottieRenderer9saveStateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer12restoreStateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingStateE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QLottieRenderer13trimmingStateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK21QLottiePrecomposition")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieLayer")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK17QLottieSolidLayer")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK16QLottieTextLayer")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieGroup")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK11QLottieRect")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK14QLottieEllipse")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK15QLottiePolyStar")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieRound")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK11QLottieFill")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieGFill")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieImage")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK13QLottieStroke")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK21QLottieBasicTransform")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK21QLottieShapeTransform")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK20QLottieFreeFormShape")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK15QLottieTrimPath")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK17QLottieFillEffect")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK15QLottieRepeater")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6finishERK12QLottieLayer")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6finishERK12QLottieGroup")) {
      taken[24] = call;
      return true;
    }
    return false;
  }

  //  void QLottieRenderer::saveState()
  void saveState() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRendererCall0 call = reinterpret_cast<CuteQLottieRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::restoreState()
  void restoreState() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRendererCall1 call = reinterpret_cast<CuteQLottieRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::setTrimmingState(TrimmingState state)
  void setTrimmingState(QLottieRenderer::TrimmingState state) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRendererCall2 call = reinterpret_cast<CuteQLottieRendererCall2>(taken[2]);
      call(this, static_cast<int>(state), &handled);
      if (handled) return;
    }
    QLottieRenderer::setTrimmingState(state);
  }

  //  TrimmingState QLottieRenderer::trimmingState() const
  QLottieRenderer::TrimmingState trimmingState() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRendererCall3 call = reinterpret_cast<CuteQLottieRendererCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLottieRenderer::TrimmingState>(given);
    }
    return QLottieRenderer::trimmingState();
  }

  //  void QLottieRenderer::render(const QLottiePrecomposition &precomp)
  void render(const QLottiePrecomposition &precomp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRendererCall4 call = reinterpret_cast<CuteQLottieRendererCall4>(taken[4]);
      call(this, &precomp, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieLayer &layer)
  void render(const QLottieLayer &layer) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRendererCall5 call = reinterpret_cast<CuteQLottieRendererCall5>(taken[5]);
      call(this, &layer, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieSolidLayer &layer)
  void render(const QLottieSolidLayer &layer) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRendererCall6 call = reinterpret_cast<CuteQLottieRendererCall6>(taken[6]);
      call(this, &layer, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieTextLayer &a0)
  void render(const QLottieTextLayer &a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieRendererCall7 call = reinterpret_cast<CuteQLottieRendererCall7>(taken[7]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::render(a0);
  }

  //  void QLottieRenderer::render(const QLottieGroup &a0)
  void render(const QLottieGroup &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieRendererCall8 call = reinterpret_cast<CuteQLottieRendererCall8>(taken[8]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::render(a0);
  }

  //  void QLottieRenderer::render(const QLottieRect &rect)
  void render(const QLottieRect &rect) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieRendererCall9 call = reinterpret_cast<CuteQLottieRendererCall9>(taken[9]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieEllipse &ellipse)
  void render(const QLottieEllipse &ellipse) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieRendererCall10 call = reinterpret_cast<CuteQLottieRendererCall10>(taken[10]);
      call(this, &ellipse, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottiePolyStar &star)
  void render(const QLottiePolyStar &star) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieRendererCall11 call = reinterpret_cast<CuteQLottieRendererCall11>(taken[11]);
      call(this, &star, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieRound &round)
  void render(const QLottieRound &round) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieRendererCall12 call = reinterpret_cast<CuteQLottieRendererCall12>(taken[12]);
      call(this, &round, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieFill &fill)
  void render(const QLottieFill &fill) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLottieRendererCall13 call = reinterpret_cast<CuteQLottieRendererCall13>(taken[13]);
      call(this, &fill, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieGFill &fill)
  void render(const QLottieGFill &fill) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLottieRendererCall14 call = reinterpret_cast<CuteQLottieRendererCall14>(taken[14]);
      call(this, &fill, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieImage &image)
  void render(const QLottieImage &image) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLottieRendererCall15 call = reinterpret_cast<CuteQLottieRendererCall15>(taken[15]);
      call(this, &image, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieStroke &stroke)
  void render(const QLottieStroke &stroke) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLottieRendererCall16 call = reinterpret_cast<CuteQLottieRendererCall16>(taken[16]);
      call(this, &stroke, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieBasicTransform &trans)
  void render(const QLottieBasicTransform &trans) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLottieRendererCall17 call = reinterpret_cast<CuteQLottieRendererCall17>(taken[17]);
      call(this, &trans, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieShapeTransform &trans)
  void render(const QLottieShapeTransform &trans) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLottieRendererCall18 call = reinterpret_cast<CuteQLottieRendererCall18>(taken[18]);
      call(this, &trans, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieFreeFormShape &shape)
  void render(const QLottieFreeFormShape &shape) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLottieRendererCall19 call = reinterpret_cast<CuteQLottieRendererCall19>(taken[19]);
      call(this, &shape, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieTrimPath &trans)
  void render(const QLottieTrimPath &trans) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLottieRendererCall20 call = reinterpret_cast<CuteQLottieRendererCall20>(taken[20]);
      call(this, &trans, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieFillEffect &effect)
  void render(const QLottieFillEffect &effect) override {
    if (taken[21]) {
      int handled = 0;
      CuteQLottieRendererCall21 call = reinterpret_cast<CuteQLottieRendererCall21>(taken[21]);
      call(this, &effect, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::render(const QLottieRepeater &repeater)
  void render(const QLottieRepeater &repeater) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLottieRendererCall22 call = reinterpret_cast<CuteQLottieRendererCall22>(taken[22]);
      call(this, &repeater, &handled);
      if (handled) return;
    }
  }

  //  void QLottieRenderer::finish(const QLottieLayer &a0)
  void finish(const QLottieLayer &a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLottieRendererCall23 call = reinterpret_cast<CuteQLottieRendererCall23>(taken[23]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::finish(a0);
  }

  //  void QLottieRenderer::finish(const QLottieGroup &a0)
  void finish(const QLottieGroup &a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQLottieRendererCall24 call = reinterpret_cast<CuteQLottieRendererCall24>(taken[24]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::finish(a0);
  }
};

//  QLottieRenderer::~QLottieRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRendererD1Ev(QLottieRenderer *self) {
  delete self;
}

//  void QLottieRenderer::saveState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer9saveStateEv(QLottieRenderer *self) {
  self->saveState();
}

//  void QLottieRenderer::restoreState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer12restoreStateEv(QLottieRenderer *self) {
  self->restoreState();
}

//  void QLottieRenderer::setTrimmingState(TrimmingState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingStateE(
    QLottieRenderer *self,
    QLottieRenderer::TrimmingState state) {
  self->setTrimmingState(state);
}

//  TrimmingState QLottieRenderer::trimmingState() const
extern "C" Q_DECL_EXPORT
QLottieRenderer::TrimmingState ritual_ZNK15QLottieRenderer13trimmingStateEv(
    const QLottieRenderer *self) {
  return self->trimmingState();
}

//  void QLottieRenderer::render(const QLottiePrecomposition &precomp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK21QLottiePrecomposition(
    QLottieRenderer *self,
    const QLottiePrecomposition *precomp) {
  self->render(*precomp);
}

//  void QLottieRenderer::render(const QLottieLayer &layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK12QLottieLayer(
    QLottieRenderer *self,
    const QLottieLayer *layer) {
  self->render(*layer);
}

//  void QLottieRenderer::render(const QLottieSolidLayer &layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK17QLottieSolidLayer(
    QLottieRenderer *self,
    const QLottieSolidLayer *layer) {
  self->render(*layer);
}

//  void QLottieRenderer::render(const QLottieTextLayer &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK16QLottieTextLayer(
    QLottieRenderer *self,
    const QLottieTextLayer *a0) {
  self->render(*a0);
}

//  void QLottieRenderer::render(const QLottieGroup &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK12QLottieGroup(
    QLottieRenderer *self,
    const QLottieGroup *a0) {
  self->render(*a0);
}

//  void QLottieRenderer::render(const QLottieRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK11QLottieRect(
    QLottieRenderer *self,
    const QLottieRect *rect) {
  self->render(*rect);
}

//  void QLottieRenderer::render(const QLottieEllipse &ellipse)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK14QLottieEllipse(
    QLottieRenderer *self,
    const QLottieEllipse *ellipse) {
  self->render(*ellipse);
}

//  void QLottieRenderer::render(const QLottiePolyStar &star)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK15QLottiePolyStar(
    QLottieRenderer *self,
    const QLottiePolyStar *star) {
  self->render(*star);
}

//  void QLottieRenderer::render(const QLottieRound &round)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK12QLottieRound(
    QLottieRenderer *self,
    const QLottieRound *round) {
  self->render(*round);
}

//  void QLottieRenderer::render(const QLottieFill &fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK11QLottieFill(
    QLottieRenderer *self,
    const QLottieFill *fill) {
  self->render(*fill);
}

//  void QLottieRenderer::render(const QLottieGFill &fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK12QLottieGFill(
    QLottieRenderer *self,
    const QLottieGFill *fill) {
  self->render(*fill);
}

//  void QLottieRenderer::render(const QLottieImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK12QLottieImage(
    QLottieRenderer *self,
    const QLottieImage *image) {
  self->render(*image);
}

//  void QLottieRenderer::render(const QLottieStroke &stroke)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK13QLottieStroke(
    QLottieRenderer *self,
    const QLottieStroke *stroke) {
  self->render(*stroke);
}

//  void QLottieRenderer::render(const QLottieBasicTransform &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK21QLottieBasicTransform(
    QLottieRenderer *self,
    const QLottieBasicTransform *trans) {
  self->render(*trans);
}

//  void QLottieRenderer::render(const QLottieShapeTransform &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK21QLottieShapeTransform(
    QLottieRenderer *self,
    const QLottieShapeTransform *trans) {
  self->render(*trans);
}

//  void QLottieRenderer::render(const QLottieFreeFormShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK20QLottieFreeFormShape(
    QLottieRenderer *self,
    const QLottieFreeFormShape *shape) {
  self->render(*shape);
}

//  void QLottieRenderer::render(const QLottieTrimPath &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK15QLottieTrimPath(
    QLottieRenderer *self,
    const QLottieTrimPath *trans) {
  self->render(*trans);
}

//  void QLottieRenderer::render(const QLottieFillEffect &effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK17QLottieFillEffect(
    QLottieRenderer *self,
    const QLottieFillEffect *effect) {
  self->render(*effect);
}

//  void QLottieRenderer::render(const QLottieRepeater &repeater)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6renderERK15QLottieRepeater(
    QLottieRenderer *self,
    const QLottieRepeater *repeater) {
  self->render(*repeater);
}

//  void QLottieRenderer::renderPathElements(const QList<QLottieBase *>
//      &pathElements)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer18renderPathElementsERK5QListIP11QLottieBaseE(
    QLottieRenderer *self,
    const QList<QLottieBase *> *pathElements) {
  self->renderPathElements(*pathElements);
}

//  void QLottieRenderer::finish(const QLottieLayer &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6finishERK12QLottieLayer(
    QLottieRenderer *self,
    const QLottieLayer *a0) {
  self->finish(*a0);
}

//  void QLottieRenderer::finish(const QLottieGroup &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer6finishERK12QLottieGroup(
    QLottieRenderer *self,
    const QLottieGroup *a0) {
  self->finish(*a0);
}

//  void QLottieRenderer::saveTrimmingState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer17saveTrimmingStateEv(QLottieRenderer *self) {
  self->saveTrimmingState();
}

//  void QLottieRenderer::restoreTrimmingState()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer20restoreTrimmingStateEv(
    QLottieRenderer *self) {
  self->restoreTrimmingState();
}

//  void QLottieRenderer::applyTransform(QTransform *xf, const
//      QLottieBasicTransform &lottieXf, bool isShapeTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QLottieRenderer14applyTransformEP10QTransformRK21QLottieBasicTransformb(
    QTransform *xf,
    const QLottieBasicTransform *lottieXf,
    bool isShapeTransform) {
  QLottieRenderer::applyTransform(xf, *lottieXf, isShapeTransform);
}

//  a Python function taken by a CuteQLottieRenderer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRenderer(
    QLottieRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRenderer *>(self)->take(key, call);
}

//  void QLottieRenderer::setTrimmingState(TrimmingState state)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingStateE(
    QLottieRenderer *self,
    QLottieRenderer::TrimmingState state) {
  self->QLottieRenderer::setTrimmingState(state);
}

//  TrimmingState QLottieRenderer::trimmingState() const
extern "C" Q_DECL_EXPORT
QLottieRenderer::TrimmingState ritual_own_ZNK15QLottieRenderer13trimmingStateEv(
    const QLottieRenderer *self) {
  return self->QLottieRenderer::trimmingState();
}

//  void QLottieRenderer::render(const QLottieTextLayer &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieRenderer6renderERK16QLottieTextLayer(
    QLottieRenderer *self,
    const QLottieTextLayer *a0) {
  self->QLottieRenderer::render(*a0);
}

//  void QLottieRenderer::render(const QLottieGroup &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieRenderer6renderERK12QLottieGroup(
    QLottieRenderer *self,
    const QLottieGroup *a0) {
  self->QLottieRenderer::render(*a0);
}

//  void QLottieRenderer::finish(const QLottieLayer &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieRenderer6finishERK12QLottieLayer(
    QLottieRenderer *self,
    const QLottieLayer *a0) {
  self->QLottieRenderer::finish(*a0);
}

//  void QLottieRenderer::finish(const QLottieGroup &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QLottieRenderer6finishERK12QLottieGroup(
    QLottieRenderer *self,
    const QLottieGroup *a0) {
  self->QLottieRenderer::finish(*a0);
}
