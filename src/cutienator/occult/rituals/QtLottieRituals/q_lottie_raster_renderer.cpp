//  Written by dev_tooling.RitualGenerator from the records of
//  QtLottie/6.12.0/QtLottie/private/qlottierasterrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLottie/QtLottie>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/6.12.0/QtLottie/private/qlottierasterrenderer_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieprecomposition_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottielayer_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottieflatlayers_p.h>
#include <QtLottie/6.12.0/QtLottie/private/qlottietextlayer_p.h>
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
#include <QtLottie/6.12.0/QtLottie/private/qlottiegroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLottie/private/qlottierasterrenderer_p.h>
#include <QPainter>
#include <QRectF>
#include <QBrush>
#include <QTransform>
#include <QGradient>
#include <QPointer>
#include <QtLottie/private/qlottieshape_p.h>
#include <QtLottie/private/qlottiefill_p.h>
#include <QtLottie/private/qlottiegfill_p.h>
#include <QtLottie/private/qlottieimage_p.h>
#include <QtLottie/private/qlottiebasictransform_p.h>
#include <QtLottie/private/qlottieshapetransform_p.h>
#include <QtLottie/private/qlottierect_p.h>
#include <QtLottie/private/qlottieellipse_p.h>
#include <QtLottie/private/qlottiepolystar_p.h>
#include <QtLottie/private/qlottieround_p.h>
#include <QtLottie/private/qlottiefreeformshape_p.h>
#include <QtLottie/private/qlottietrimpath_p.h>
#include <QtLottie/private/qlottiefilleffect_p.h>
#include <QtLottie/private/qlottierepeater_p.h>
#include <QtLottie/private/qlottieflatlayers_p.h>
#include <QtLottie/private/qlottieprecomposition_p.h>
#include <QtLottie/private/qlottietextlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlottie/src/lottie/renderer/qlottierasterrenderer.cpp, line 52, as _ZN21QLottieRasterRenderer12restoreStateEv
inline void QLottieRasterRenderer::restoreState()
{
    qCDebug(lcLottieQtLottieRender) << "Restore painter state";
    m_painter->restore();
    restoreTrimmingState();
    m_unitedPath = m_pathStack.pop();
    m_renderPath.setFillRule(m_unitedPath.fillRule());
    m_clipPath.setFillRule(m_unitedPath.fillRule());
    m_fillEffect = m_fillEffectStack.pop();
    m_inverseFillTransform = m_inverseFillTransformStack.pop();
}

//  from ../qtlottie/src/lottie/renderer/qlottierasterrenderer.cpp, line 306, as _ZN21QLottieRasterRenderer18renderPathElementsERK5QListIP11QLottieBaseE
inline void QLottieRasterRenderer::renderPathElements(const QList<QLottieBase *> &pathElements)
{
    qCDebug(lcLottieQtLottieRender) << "PathElements: count:" << pathElements.size();

    m_painter->save();

    m_renderPath.clear();
    for (const QLottieBase *element : pathElements)
        element->render(*this); // Accumulates element paths in m_renderPath

    for (int i = 0; i < m_repeatCount; i++) {
        if (i > 0)
            qCDebug(lcLottieQtLottieRender) << "Render repeated, combined path, iteration" << i + 1;
        applyRepeaterTransform(i);
        if (trimmingState() == QLottieRenderer::Sequential) {
            QTransform t = m_painter->transform();
            QPainterPath tp = t.map(m_renderPath);
            tp.addPath(m_unitedPath);
            m_unitedPath = tp;
        } else if (m_buildingClipRegion) {
            QTransform t = m_painter->transform();
            QPainterPath tp = t.map(m_renderPath);
            tp.addPath(m_clipPath);
            m_clipPath = tp;
        } else {
            if (!m_inverseFillTransform.isIdentity() && m_painter->brush().gradient()) {
                bool fill_ok = false;
                const QTransform fillTransform = m_inverseFillTransform.inverted(&fill_ok);
                if (fill_ok) {
                    QBrush adjustedBrush = m_painter->brush();
                    adjustedBrush.setTransform(fillTransform);
                    m_painter->save();
                    m_painter->setBrush(adjustedBrush);
                    m_painter->drawPath(m_renderPath);
                    m_painter->restore();
                } else {
                    m_painter->drawPath(m_renderPath);
                }
            } else {
                m_painter->drawPath(m_renderPath);
            }
        }
    }

    m_painter->restore();
}

//  from ../qtlottie/src/lottie/renderer/qlottierasterrenderer.cpp, line 41, as _ZN21QLottieRasterRenderer9saveStateEv
inline void QLottieRasterRenderer::saveState()
{
    qCDebug(lcLottieQtLottieRender) << "Save painter state";
    m_painter->save();
    saveTrimmingState();
    m_pathStack.push_back(m_unitedPath);
    m_fillEffectStack.push_back(m_fillEffect);
    m_inverseFillTransformStack.push(m_inverseFillTransform);
    m_unitedPath.clear();
}

//  from ../qtlottie/src/lottie/renderer/qlottierasterrenderer.cpp, line 353, as _ZN21QLottieRasterRenderer22applyRepeaterTransformEi
inline void QLottieRasterRenderer::applyRepeaterTransform(int instance)
{
    if (!m_repeaterTransform || instance == 0)
        return;

    QTransform t = m_painter->transform();

    QPointF anchors = -m_repeaterTransform->anchorPoint();
    QPointF position = m_repeaterTransform->position();
    QPointF anchoredCenter = anchors + position;

    t.translate(anchoredCenter.x(), anchoredCenter.y());
    t.rotate(m_repeaterTransform->rotation());
    t.scale(m_repeaterTransform->scale().x(),
            m_repeaterTransform->scale().y());
    m_painter->setTransform(t);

    qreal o =m_repeaterTransform->opacityAtInstance(instance);

    m_painter->setOpacity(m_painter->opacity() * o);
}
//  -----------------------------------------------------------------------

//  A QLottieRasterRenderer that Python can take functions over in. Every QLottieRasterRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQLottieRasterRendererCall0)(const void *, int *);
typedef void (*CuteQLottieRasterRendererCall1)(const void *, int *);
typedef void (*CuteQLottieRasterRendererCall2)(const void *, const QLottiePrecomposition *, int *);
typedef void (*CuteQLottieRasterRendererCall3)(const void *, const QLottieLayer *, int *);
typedef void (*CuteQLottieRasterRendererCall4)(const void *, const QLottieSolidLayer *, int *);
typedef void (*CuteQLottieRasterRendererCall5)(const void *, const QLottieTextLayer *, int *);
typedef void (*CuteQLottieRasterRendererCall6)(const void *, const QLottieRect *, int *);
typedef void (*CuteQLottieRasterRendererCall7)(const void *, const QLottieEllipse *, int *);
typedef void (*CuteQLottieRasterRendererCall8)(const void *, const QLottiePolyStar *, int *);
typedef void (*CuteQLottieRasterRendererCall9)(const void *, const QLottieRound *, int *);
typedef void (*CuteQLottieRasterRendererCall10)(const void *, const QLottieFill *, int *);
typedef void (*CuteQLottieRasterRendererCall11)(const void *, const QLottieGFill *, int *);
typedef void (*CuteQLottieRasterRendererCall12)(const void *, const QLottieImage *, int *);
typedef void (*CuteQLottieRasterRendererCall13)(const void *, const QLottieStroke *, int *);
typedef void (*CuteQLottieRasterRendererCall14)(const void *, const QLottieBasicTransform *, int *);
typedef void (*CuteQLottieRasterRendererCall15)(const void *, const QLottieShapeTransform *, int *);
typedef void (*CuteQLottieRasterRendererCall16)(const void *, const QLottieFreeFormShape *, int *);
typedef void (*CuteQLottieRasterRendererCall17)(const void *, const QLottieTrimPath *, int *);
typedef void (*CuteQLottieRasterRendererCall18)(const void *, const QLottieFillEffect *, int *);
typedef void (*CuteQLottieRasterRendererCall19)(const void *, const QLottieRepeater *, int *);
typedef void (*CuteQLottieRasterRendererCall20)(const void *, int, int *);
typedef int (*CuteQLottieRasterRendererCall21)(const void *, int *);
typedef void (*CuteQLottieRasterRendererCall22)(const void *, const QLottieGroup *, int *);
typedef void (*CuteQLottieRasterRendererCall23)(const void *, const QLottieLayer *, int *);
typedef void (*CuteQLottieRasterRendererCall24)(const void *, const QLottieGroup *, int *);
class CuteQLottieRasterRenderer : public QLottieRasterRenderer {
public:
  using QLottieRasterRenderer::QLottieRasterRenderer;
  CuteQLottieRasterRenderer(const QLottieRasterRenderer & other) : QLottieRasterRenderer(other) {}
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
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK21QLottiePrecomposition")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieLayer")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK17QLottieSolidLayer")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK16QLottieTextLayer")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK11QLottieRect")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK14QLottieEllipse")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK15QLottiePolyStar")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieRound")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK11QLottieFill")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieGFill")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieImage")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK13QLottieStroke")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK21QLottieBasicTransform")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK21QLottieShapeTransform")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK20QLottieFreeFormShape")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK15QLottieTrimPath")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK17QLottieFillEffect")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK15QLottieRepeater")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer16setTrimmingStateENS_13TrimmingStateE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK15QLottieRenderer13trimmingStateEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QLottieRenderer6renderERK12QLottieGroup")) {
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

  //  void QLottieRasterRenderer::saveState()
  void saveState() override {
    if (taken[0]) {
      int handled = 0;
      CuteQLottieRasterRendererCall0 call = reinterpret_cast<CuteQLottieRasterRendererCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::saveState();
  }

  //  void QLottieRasterRenderer::restoreState()
  void restoreState() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLottieRasterRendererCall1 call = reinterpret_cast<CuteQLottieRasterRendererCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::restoreState();
  }

  //  void QLottieRasterRenderer::render(const QLottiePrecomposition
  //      &precomp)
  void render(const QLottiePrecomposition &precomp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLottieRasterRendererCall2 call = reinterpret_cast<CuteQLottieRasterRendererCall2>(taken[2]);
      call(this, &precomp, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(precomp);
  }

  //  void QLottieRasterRenderer::render(const QLottieLayer &layer)
  void render(const QLottieLayer &layer) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLottieRasterRendererCall3 call = reinterpret_cast<CuteQLottieRasterRendererCall3>(taken[3]);
      call(this, &layer, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(layer);
  }

  //  void QLottieRasterRenderer::render(const QLottieSolidLayer &layer)
  void render(const QLottieSolidLayer &layer) override {
    if (taken[4]) {
      int handled = 0;
      CuteQLottieRasterRendererCall4 call = reinterpret_cast<CuteQLottieRasterRendererCall4>(taken[4]);
      call(this, &layer, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(layer);
  }

  //  void QLottieRasterRenderer::render(const QLottieTextLayer &layer)
  void render(const QLottieTextLayer &layer) override {
    if (taken[5]) {
      int handled = 0;
      CuteQLottieRasterRendererCall5 call = reinterpret_cast<CuteQLottieRasterRendererCall5>(taken[5]);
      call(this, &layer, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(layer);
  }

  //  void QLottieRasterRenderer::render(const QLottieRect &rect)
  void render(const QLottieRect &rect) override {
    if (taken[6]) {
      int handled = 0;
      CuteQLottieRasterRendererCall6 call = reinterpret_cast<CuteQLottieRasterRendererCall6>(taken[6]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(rect);
  }

  //  void QLottieRasterRenderer::render(const QLottieEllipse &ellipse)
  void render(const QLottieEllipse &ellipse) override {
    if (taken[7]) {
      int handled = 0;
      CuteQLottieRasterRendererCall7 call = reinterpret_cast<CuteQLottieRasterRendererCall7>(taken[7]);
      call(this, &ellipse, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(ellipse);
  }

  //  void QLottieRasterRenderer::render(const QLottiePolyStar &star)
  void render(const QLottiePolyStar &star) override {
    if (taken[8]) {
      int handled = 0;
      CuteQLottieRasterRendererCall8 call = reinterpret_cast<CuteQLottieRasterRendererCall8>(taken[8]);
      call(this, &star, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(star);
  }

  //  void QLottieRasterRenderer::render(const QLottieRound &round)
  void render(const QLottieRound &round) override {
    if (taken[9]) {
      int handled = 0;
      CuteQLottieRasterRendererCall9 call = reinterpret_cast<CuteQLottieRasterRendererCall9>(taken[9]);
      call(this, &round, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(round);
  }

  //  void QLottieRasterRenderer::render(const QLottieFill &fill)
  void render(const QLottieFill &fill) override {
    if (taken[10]) {
      int handled = 0;
      CuteQLottieRasterRendererCall10 call = reinterpret_cast<CuteQLottieRasterRendererCall10>(taken[10]);
      call(this, &fill, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(fill);
  }

  //  void QLottieRasterRenderer::render(const QLottieGFill &shape)
  void render(const QLottieGFill &shape) override {
    if (taken[11]) {
      int handled = 0;
      CuteQLottieRasterRendererCall11 call = reinterpret_cast<CuteQLottieRasterRendererCall11>(taken[11]);
      call(this, &shape, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(shape);
  }

  //  void QLottieRasterRenderer::render(const QLottieImage &image)
  void render(const QLottieImage &image) override {
    if (taken[12]) {
      int handled = 0;
      CuteQLottieRasterRendererCall12 call = reinterpret_cast<CuteQLottieRasterRendererCall12>(taken[12]);
      call(this, &image, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(image);
  }

  //  void QLottieRasterRenderer::render(const QLottieStroke &stroke)
  void render(const QLottieStroke &stroke) override {
    if (taken[13]) {
      int handled = 0;
      CuteQLottieRasterRendererCall13 call = reinterpret_cast<CuteQLottieRasterRendererCall13>(taken[13]);
      call(this, &stroke, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(stroke);
  }

  //  void QLottieRasterRenderer::render(const QLottieBasicTransform
  //      &transform)
  void render(const QLottieBasicTransform &transform) override {
    if (taken[14]) {
      int handled = 0;
      CuteQLottieRasterRendererCall14 call = reinterpret_cast<CuteQLottieRasterRendererCall14>(taken[14]);
      call(this, &transform, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(transform);
  }

  //  void QLottieRasterRenderer::render(const QLottieShapeTransform
  //      &transform)
  void render(const QLottieShapeTransform &transform) override {
    if (taken[15]) {
      int handled = 0;
      CuteQLottieRasterRendererCall15 call = reinterpret_cast<CuteQLottieRasterRendererCall15>(taken[15]);
      call(this, &transform, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(transform);
  }

  //  void QLottieRasterRenderer::render(const QLottieFreeFormShape &shape)
  void render(const QLottieFreeFormShape &shape) override {
    if (taken[16]) {
      int handled = 0;
      CuteQLottieRasterRendererCall16 call = reinterpret_cast<CuteQLottieRasterRendererCall16>(taken[16]);
      call(this, &shape, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(shape);
  }

  //  void QLottieRasterRenderer::render(const QLottieTrimPath &trans)
  void render(const QLottieTrimPath &trans) override {
    if (taken[17]) {
      int handled = 0;
      CuteQLottieRasterRendererCall17 call = reinterpret_cast<CuteQLottieRasterRendererCall17>(taken[17]);
      call(this, &trans, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(trans);
  }

  //  void QLottieRasterRenderer::render(const QLottieFillEffect &effect)
  void render(const QLottieFillEffect &effect) override {
    if (taken[18]) {
      int handled = 0;
      CuteQLottieRasterRendererCall18 call = reinterpret_cast<CuteQLottieRasterRendererCall18>(taken[18]);
      call(this, &effect, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(effect);
  }

  //  void QLottieRasterRenderer::render(const QLottieRepeater &repeater)
  void render(const QLottieRepeater &repeater) override {
    if (taken[19]) {
      int handled = 0;
      CuteQLottieRasterRendererCall19 call = reinterpret_cast<CuteQLottieRasterRendererCall19>(taken[19]);
      call(this, &repeater, &handled);
      if (handled) return;
    }
    QLottieRasterRenderer::render(repeater);
  }

  //  void QLottieRenderer::setTrimmingState(TrimmingState state)
  void setTrimmingState(QLottieRenderer::TrimmingState state) override {
    if (taken[20]) {
      int handled = 0;
      CuteQLottieRasterRendererCall20 call = reinterpret_cast<CuteQLottieRasterRendererCall20>(taken[20]);
      call(this, static_cast<int>(state), &handled);
      if (handled) return;
    }
    QLottieRenderer::setTrimmingState(state);
  }

  //  TrimmingState QLottieRenderer::trimmingState() const
  QLottieRenderer::TrimmingState trimmingState() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQLottieRasterRendererCall21 call = reinterpret_cast<CuteQLottieRasterRendererCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return static_cast<QLottieRenderer::TrimmingState>(given);
    }
    return QLottieRenderer::trimmingState();
  }

  //  void QLottieRenderer::render(const QLottieGroup &a0)
  void render(const QLottieGroup &a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQLottieRasterRendererCall22 call = reinterpret_cast<CuteQLottieRasterRendererCall22>(taken[22]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::render(a0);
  }

  //  void QLottieRenderer::finish(const QLottieLayer &a0)
  void finish(const QLottieLayer &a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQLottieRasterRendererCall23 call = reinterpret_cast<CuteQLottieRasterRendererCall23>(taken[23]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::finish(a0);
  }

  //  void QLottieRenderer::finish(const QLottieGroup &a0)
  void finish(const QLottieGroup &a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQLottieRasterRendererCall24 call = reinterpret_cast<CuteQLottieRasterRendererCall24>(taken[24]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QLottieRenderer::finish(a0);
  }
};

//  QLottieRasterRenderer::~QLottieRasterRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRendererD1Ev(QLottieRasterRenderer *self) {
  delete self;
}

//  void QLottieRasterRenderer::saveState()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer9saveStateEv(
    QLottieRasterRenderer *self) {
  self->saveState();
}

//  void QLottieRasterRenderer::restoreState()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer12restoreStateEv(
    QLottieRasterRenderer *self) {
  self->restoreState();
}

//  void QLottieRasterRenderer::render(const QLottiePrecomposition &precomp)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK21QLottiePrecomposition(
    QLottieRasterRenderer *self,
    const QLottiePrecomposition *precomp) {
  self->render(*precomp);
}

//  void QLottieRasterRenderer::render(const QLottieLayer &layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK12QLottieLayer(
    QLottieRasterRenderer *self,
    const QLottieLayer *layer) {
  self->render(*layer);
}

//  void QLottieRasterRenderer::render(const QLottieSolidLayer &layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK17QLottieSolidLayer(
    QLottieRasterRenderer *self,
    const QLottieSolidLayer *layer) {
  self->render(*layer);
}

//  void QLottieRasterRenderer::render(const QLottieTextLayer &layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK16QLottieTextLayer(
    QLottieRasterRenderer *self,
    const QLottieTextLayer *layer) {
  self->render(*layer);
}

//  void QLottieRasterRenderer::render(const QLottieRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK11QLottieRect(
    QLottieRasterRenderer *self,
    const QLottieRect *rect) {
  self->render(*rect);
}

//  void QLottieRasterRenderer::render(const QLottieEllipse &ellipse)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK14QLottieEllipse(
    QLottieRasterRenderer *self,
    const QLottieEllipse *ellipse) {
  self->render(*ellipse);
}

//  void QLottieRasterRenderer::render(const QLottiePolyStar &star)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK15QLottiePolyStar(
    QLottieRasterRenderer *self,
    const QLottiePolyStar *star) {
  self->render(*star);
}

//  void QLottieRasterRenderer::render(const QLottieRound &round)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK12QLottieRound(
    QLottieRasterRenderer *self,
    const QLottieRound *round) {
  self->render(*round);
}

//  void QLottieRasterRenderer::render(const QLottieFill &fill)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK11QLottieFill(
    QLottieRasterRenderer *self,
    const QLottieFill *fill) {
  self->render(*fill);
}

//  void QLottieRasterRenderer::render(const QLottieGFill &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK12QLottieGFill(
    QLottieRasterRenderer *self,
    const QLottieGFill *shape) {
  self->render(*shape);
}

//  void QLottieRasterRenderer::render(const QLottieImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK12QLottieImage(
    QLottieRasterRenderer *self,
    const QLottieImage *image) {
  self->render(*image);
}

//  void QLottieRasterRenderer::render(const QLottieStroke &stroke)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK13QLottieStroke(
    QLottieRasterRenderer *self,
    const QLottieStroke *stroke) {
  self->render(*stroke);
}

//  void QLottieRasterRenderer::render(const QLottieBasicTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK21QLottieBasicTransform(
    QLottieRasterRenderer *self,
    const QLottieBasicTransform *transform) {
  self->render(*transform);
}

//  void QLottieRasterRenderer::render(const QLottieShapeTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK21QLottieShapeTransform(
    QLottieRasterRenderer *self,
    const QLottieShapeTransform *transform) {
  self->render(*transform);
}

//  void QLottieRasterRenderer::render(const QLottieFreeFormShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK20QLottieFreeFormShape(
    QLottieRasterRenderer *self,
    const QLottieFreeFormShape *shape) {
  self->render(*shape);
}

//  void QLottieRasterRenderer::render(const QLottieTrimPath &trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK15QLottieTrimPath(
    QLottieRasterRenderer *self,
    const QLottieTrimPath *trans) {
  self->render(*trans);
}

//  void QLottieRasterRenderer::render(const QLottieFillEffect &effect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK17QLottieFillEffect(
    QLottieRasterRenderer *self,
    const QLottieFillEffect *effect) {
  self->render(*effect);
}

//  void QLottieRasterRenderer::render(const QLottieRepeater &repeater)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer6renderERK15QLottieRepeater(
    QLottieRasterRenderer *self,
    const QLottieRepeater *repeater) {
  self->render(*repeater);
}

//  void QLottieRasterRenderer::renderPathElements(const QList<QLottieBase *>
//      &pathElements)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer18renderPathElementsERK5QListIP11QLottieBaseE(
    QLottieRasterRenderer *self,
    const QList<QLottieBase *> *pathElements) {
  self->renderPathElements(*pathElements);
}

//  void QLottieRasterRenderer::applyRepeaterTransform(int instance)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLottieRasterRenderer22applyRepeaterTransformEi(
    QLottieRasterRenderer *self,
    int instance) {
  self->applyRepeaterTransform(instance);
}

//  a Python function taken by a CuteQLottieRasterRenderer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLottieRasterRenderer(
    QLottieRasterRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLottieRasterRenderer *>(self)->take(key, call);
}
