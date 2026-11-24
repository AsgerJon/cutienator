//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisticker_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/axisticker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/axisticker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 31, as _ZN10AxisTicker12setupShadersEv
inline void AxisTicker::setupShaders()
{
    if (m_isHorizontal) {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/tickershaderhorizontal.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/tickershaderhorizontal.vert.qsb")));
    } else {
        setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/tickershader.frag.qsb")));
        setVertexShader(QUrl(QStringLiteral("qrc:/shaders/tickershader.vert.qsb")));
    }
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 42, as _ZNK10AxisTicker11iResolutionEv
inline QVector3D AxisTicker::iResolution() const
{
    return m_iResolution;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 47, as _ZNK10AxisTicker9smoothingEv
inline qreal AxisTicker::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 60, as _ZNK10AxisTicker5origoEv
inline int AxisTicker::origo() const
{
    return m_origo;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 73, as _ZNK10AxisTicker15subTicksVisibleEv
inline bool AxisTicker::subTicksVisible() const
{
    return m_subTicksVisible;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 86, as _ZNK10AxisTicker7spacingEv
inline qreal AxisTicker::spacing() const
{
    return m_spacing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 99, as _ZNK10AxisTicker12displacementEv
inline qreal AxisTicker::displacement() const
{
    return m_displacement;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 112, as _ZNK10AxisTicker12subTickColorEv
inline QColor AxisTicker::subTickColor() const
{
    return m_subTickColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 125, as _ZNK10AxisTicker9tickColorEv
inline QColor AxisTicker::tickColor() const
{
    return m_tickColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 138, as _ZNK10AxisTicker16subTickLineWidthEv
inline qreal AxisTicker::subTickLineWidth() const
{
    return m_subTickLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 151, as _ZNK10AxisTicker13tickLineWidthEv
inline qreal AxisTicker::tickLineWidth() const
{
    return m_tickLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 164, as _ZNK10AxisTicker12subTickScaleEv
inline qreal AxisTicker::subTickScale() const
{
    return m_subTickScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 177, as _ZNK10AxisTicker13subTickLengthEv
inline qreal AxisTicker::subTickLength() const
{
    return m_subTickLength;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 190, as _ZNK10AxisTicker12isHorizontalEv
inline bool AxisTicker::isHorizontal() const
{
    return m_isHorizontal;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 204, as _ZNK10AxisTicker9isFlippedEv
inline bool AxisTicker::isFlipped() const
{
    return m_flipped;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 217, as _ZNK10AxisTicker13isLogarithmicEv
inline bool AxisTicker::isLogarithmic() const
{
    return m_isLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 231, as _ZNK10AxisTicker4baseEv
inline qreal AxisTicker::base() const
{
    return m_base;
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 17, as _ZN10AxisTicker17componentCompleteEv
inline void AxisTicker::componentComplete()
{
    QQuickShaderEffect::componentComplete();
    setupShaders();
}

//  from ../qtgraphs/src/graphs2d/axis/axisticker.cpp, line 23, as _ZN10AxisTicker14geometryChangeERK6QRectFS2_
inline void AxisTicker::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    m_iResolution = QVector3D(newGeometry.width(), newGeometry.height(), 1.0);
    emit iResolutionChanged();

    QQuickShaderEffect::geometryChange(newGeometry, oldGeometry);
}
//  -----------------------------------------------------------------------

//  Only a class built on AxisTicker may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAxisTicker : AxisTicker {
  using AxisTicker::componentComplete;
};

//  A AxisTicker that Python can take functions over in. Every AxisTicker
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAxisTickerCall0)(const void *, int *);
typedef void (*CuteAxisTickerCall1)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteAxisTickerCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteAxisTickerCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteAxisTickerCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteAxisTickerCall5)(const void *, int *);
typedef const QRectF * (*CuteAxisTickerCall6)(const void *, int *);
typedef bool (*CuteAxisTickerCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAxisTickerCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAxisTickerCall9)(const void *, int *);
typedef void * (*CuteAxisTickerCall10)(const void *, int *);
typedef void (*CuteAxisTickerCall11)(const void *, int *);
typedef void (*CuteAxisTickerCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteAxisTickerCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAxisTickerCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAxisTickerCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisTickerCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisTickerCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisTickerCall21)(const void *, int *);
typedef void (*CuteAxisTickerCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAxisTickerCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAxisTickerCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteAxisTickerCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisTickerCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisTickerCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisTickerCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAxisTickerCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteAxisTickerCall33)(const void *, int *);
typedef void (*CuteAxisTickerCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisTickerCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisTickerCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisTicker : public AxisTicker {
public:
  using AxisTicker::AxisTicker;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_shadereffect)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void AxisTicker::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisTickerCall0 call = reinterpret_cast<CuteAxisTickerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    AxisTicker::componentComplete();
  }

  //  void AxisTicker::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisTickerCall1 call = reinterpret_cast<CuteAxisTickerCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    AxisTicker::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffect::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisTickerCall2 call = reinterpret_cast<CuteAxisTickerCall2>(taken[2]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickShaderEffect::event(e);
  }
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(quick_shadereffect)
  //  QSGNode *QQuickShaderEffect::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *updatePaintNodeData)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *updatePaintNodeData) override {
    if (taken[3]) {
      int handled = 0;
      CuteAxisTickerCall3 call = reinterpret_cast<CuteAxisTickerCall3>(taken[3]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShaderEffect::updatePaintNode(oldNode, updatePaintNodeData);
  }
#endif  // QT_CONFIG(quick_shadereffect)

#if QT_CONFIG(quick_shadereffect)
  //  void QQuickShaderEffect::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[4]) {
      int handled = 0;
      CuteAxisTickerCall4 call = reinterpret_cast<CuteAxisTickerCall4>(taken[4]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickShaderEffect::itemChange(change, value);
  }
#endif  // QT_CONFIG(quick_shadereffect)

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteAxisTickerCall5 call = reinterpret_cast<CuteAxisTickerCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteAxisTickerCall6 call = reinterpret_cast<CuteAxisTickerCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteAxisTickerCall7 call = reinterpret_cast<CuteAxisTickerCall7>(taken[7]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteAxisTickerCall8 call = reinterpret_cast<CuteAxisTickerCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteAxisTickerCall9 call = reinterpret_cast<CuteAxisTickerCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAxisTickerCall10 call = reinterpret_cast<CuteAxisTickerCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteAxisTickerCall11 call = reinterpret_cast<CuteAxisTickerCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAxisTickerCall12 call = reinterpret_cast<CuteAxisTickerCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteAxisTickerCall13 call = reinterpret_cast<CuteAxisTickerCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteAxisTickerCall14 call = reinterpret_cast<CuteAxisTickerCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteAxisTickerCall15 call = reinterpret_cast<CuteAxisTickerCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteAxisTickerCall16 call = reinterpret_cast<CuteAxisTickerCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAxisTickerCall17 call = reinterpret_cast<CuteAxisTickerCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAxisTickerCall18 call = reinterpret_cast<CuteAxisTickerCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAxisTickerCall19 call = reinterpret_cast<CuteAxisTickerCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteAxisTickerCall20 call = reinterpret_cast<CuteAxisTickerCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAxisTickerCall21 call = reinterpret_cast<CuteAxisTickerCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteAxisTickerCall22 call = reinterpret_cast<CuteAxisTickerCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteAxisTickerCall23 call = reinterpret_cast<CuteAxisTickerCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteAxisTickerCall24 call = reinterpret_cast<CuteAxisTickerCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAxisTickerCall25 call = reinterpret_cast<CuteAxisTickerCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAxisTickerCall26 call = reinterpret_cast<CuteAxisTickerCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteAxisTickerCall27 call = reinterpret_cast<CuteAxisTickerCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteAxisTickerCall28 call = reinterpret_cast<CuteAxisTickerCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteAxisTickerCall29 call = reinterpret_cast<CuteAxisTickerCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteAxisTickerCall30 call = reinterpret_cast<CuteAxisTickerCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteAxisTickerCall31 call = reinterpret_cast<CuteAxisTickerCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteAxisTickerCall32 call = reinterpret_cast<CuteAxisTickerCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAxisTickerCall33 call = reinterpret_cast<CuteAxisTickerCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAxisTickerCall34 call = reinterpret_cast<CuteAxisTickerCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteAxisTickerCall35 call = reinterpret_cast<CuteAxisTickerCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteAxisTickerCall36 call = reinterpret_cast<CuteAxisTickerCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteAxisTickerCall37 call = reinterpret_cast<CuteAxisTickerCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteAxisTickerCall38 call = reinterpret_cast<CuteAxisTickerCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteAxisTickerCall39 call = reinterpret_cast<CuteAxisTickerCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteAxisTickerCall40 call = reinterpret_cast<CuteAxisTickerCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisTicker::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10AxisTicker10metaObjectEv(
    const AxisTicker *self) {
  return self->metaObject();
}

//  void AxisTicker::setupShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker12setupShadersEv(AxisTicker *self) {
  self->setupShaders();
}

//  QVector3D AxisTicker::iResolution() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10AxisTicker11iResolutionEv(const AxisTicker *self) {
  return new QVector3D(self->iResolution());
}

//  qreal AxisTicker::smoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker9smoothingEv(const AxisTicker *self) {
  return self->smoothing();
}

//  int AxisTicker::origo() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10AxisTicker5origoEv(const AxisTicker *self) {
  return self->origo();
}

//  bool AxisTicker::subTicksVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker15subTicksVisibleEv(const AxisTicker *self) {
  return self->subTicksVisible();
}

//  qreal AxisTicker::spacing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker7spacingEv(const AxisTicker *self) {
  return self->spacing();
}

//  qreal AxisTicker::displacement() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker12displacementEv(const AxisTicker *self) {
  return self->displacement();
}

//  QColor AxisTicker::subTickColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10AxisTicker12subTickColorEv(const AxisTicker *self) {
  return new QColor(self->subTickColor());
}

//  QColor AxisTicker::tickColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10AxisTicker9tickColorEv(const AxisTicker *self) {
  return new QColor(self->tickColor());
}

//  qreal AxisTicker::subTickLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker16subTickLineWidthEv(const AxisTicker *self) {
  return self->subTickLineWidth();
}

//  qreal AxisTicker::tickLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker13tickLineWidthEv(const AxisTicker *self) {
  return self->tickLineWidth();
}

//  qreal AxisTicker::subTickScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker12subTickScaleEv(const AxisTicker *self) {
  return self->subTickScale();
}

//  qreal AxisTicker::subTickLength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker13subTickLengthEv(const AxisTicker *self) {
  return self->subTickLength();
}

//  bool AxisTicker::isHorizontal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker12isHorizontalEv(const AxisTicker *self) {
  return self->isHorizontal();
}

//  bool AxisTicker::isFlipped() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker9isFlippedEv(const AxisTicker *self) {
  return self->isFlipped();
}

//  bool AxisTicker::isLogarithmic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10AxisTicker13isLogarithmicEv(const AxisTicker *self) {
  return self->isLogarithmic();
}

//  qreal AxisTicker::base() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10AxisTicker4baseEv(const AxisTicker *self) {
  return self->base();
}

//  void AxisTicker::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker17componentCompleteEv(AxisTicker *self) {
  self->componentComplete();
}

//  void AxisTicker::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN10AxisTicker14geometryChangeERK6QRectFS2_(
    AxisTicker *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  a Python function taken by a CuteAxisTicker, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisTicker(AxisTicker *self, const char *key, void *call) {
  return static_cast<CuteAxisTicker *>(self)->take(key, call);
}

//  void AxisTicker::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10AxisTicker17componentCompleteEv(AxisTicker *self) {
  static_cast<OwnAxisTicker *>(self)->OwnAxisTicker::componentComplete();
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
