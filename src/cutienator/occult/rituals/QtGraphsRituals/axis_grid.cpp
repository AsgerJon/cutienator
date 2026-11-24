//  Written by dev_tooling.RitualGenerator from the records of
//  QtGraphs/6.12.0/QtGraphs/private/axisgrid_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGraphs/qgraphsglobal.h>
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#if !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
#include <QtGraphs/6.12.0/QtGraphs/private/qgraphsglobal_p.h>
#include <QtGraphs/QtGraphs>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/6.12.0/QtGraphs/private/axisgrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGraphs/private/axisgrid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 31, as _ZN8AxisGrid12setupShadersEv
inline void AxisGrid::setupShaders()
{
    setFragmentShader(QUrl(QStringLiteral("qrc:/shaders/gridshader.frag.qsb")));
    setVertexShader(QUrl(QStringLiteral("qrc:/shaders/gridshader.vert.qsb")));
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 37, as _ZNK8AxisGrid11iResolutionEv
inline QVector3D AxisGrid::iResolution() const
{
    return m_iResolution;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 42, as _ZNK8AxisGrid9smoothingEv
inline qreal AxisGrid::smoothing() const
{
    return m_smoothing;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 55, as _ZNK8AxisGrid5origoEv
inline int AxisGrid::origo() const
{
    return m_origo;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 68, as _ZNK8AxisGrid14gridVisibilityEv
inline QVector4D AxisGrid::gridVisibility() const
{
    return m_gridVisibility;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 81, as _ZNK8AxisGrid9gridWidthEv
inline qreal AxisGrid::gridWidth() const
{
    return m_gridWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 94, as _ZNK8AxisGrid10gridHeightEv
inline qreal AxisGrid::gridHeight() const
{
    return m_gridHeight;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 107, as _ZNK8AxisGrid12gridMovementEv
inline QPointF AxisGrid::gridMovement() const
{
    return m_gridMovement;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 120, as _ZNK8AxisGrid12subGridColorEv
inline QColor AxisGrid::subGridColor() const
{
    return m_subGridColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 133, as _ZNK8AxisGrid9gridColorEv
inline QColor AxisGrid::gridColor() const
{
    return m_gridColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 146, as _ZNK8AxisGrid23plotAreaBackgroundColorEv
inline QColor AxisGrid::plotAreaBackgroundColor() const
{
    return m_plotAreaBackgroundColor;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 159, as _ZNK8AxisGrid16subGridLineWidthEv
inline qreal AxisGrid::subGridLineWidth() const
{
    return m_subGridLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 172, as _ZNK8AxisGrid13gridLineWidthEv
inline qreal AxisGrid::gridLineWidth() const
{
    return m_gridLineWidth;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 185, as _ZNK8AxisGrid20verticalSubGridScaleEv
inline qreal AxisGrid::verticalSubGridScale() const
{
    return m_verticalSubGridScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 198, as _ZNK8AxisGrid22horizontalSubGridScaleEv
inline qreal AxisGrid::horizontalSubGridScale() const
{
    return m_horizontalSubGridScale;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 211, as _ZNK8AxisGrid21isVerticalLogarithmicEv
inline bool AxisGrid::isVerticalLogarithmic() const
{
    return m_isVerticalLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 224, as _ZNK8AxisGrid23isHorizontalLogarithmicEv
inline bool AxisGrid::isHorizontalLogarithmic() const
{
    return m_isHorizontalLogarithmic;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 237, as _ZNK8AxisGrid12verticalBaseEv
inline qreal AxisGrid::verticalBase() const
{
    return m_verticalBase;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 250, as _ZNK8AxisGrid14horizontalBaseEv
inline qreal AxisGrid::horizontalBase() const
{
    return m_horizontalBase;
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 17, as _ZN8AxisGrid17componentCompleteEv
inline void AxisGrid::componentComplete()
{
    QQuickShaderEffect::componentComplete();
    setupShaders();
}

//  from ../qtgraphs/src/graphs2d/axis/axisgrid.cpp, line 23, as _ZN8AxisGrid14geometryChangeERK6QRectFS2_
inline void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF &oldGeometry)
{
    m_iResolution = QVector3D(newGeometry.width(), newGeometry.height(), 1.0);
    emit iResolutionChanged();

    QQuickShaderEffect::geometryChange(newGeometry, oldGeometry);
}
//  -----------------------------------------------------------------------

//  Only a class built on AxisGrid may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnAxisGrid : AxisGrid {
  using AxisGrid::componentComplete;
};

//  A AxisGrid that Python can take functions over in. Every AxisGrid
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteAxisGridCall0)(const void *, int *);
typedef void (*CuteAxisGridCall1)(const void *, const QRectF *, const QRectF *, int *);
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef bool (*CuteAxisGridCall2)(const void *, QEvent *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
typedef void * (*CuteAxisGridCall3)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
#if QT_CONFIG(quick_shadereffect)
typedef void (*CuteAxisGridCall4)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#endif  // QT_CONFIG(quick_shadereffect)
typedef const QRectF * (*CuteAxisGridCall5)(const void *, int *);
typedef const QRectF * (*CuteAxisGridCall6)(const void *, int *);
typedef bool (*CuteAxisGridCall7)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteAxisGridCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteAxisGridCall9)(const void *, int *);
typedef void * (*CuteAxisGridCall10)(const void *, int *);
typedef void (*CuteAxisGridCall11)(const void *, int *);
typedef void (*CuteAxisGridCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteAxisGridCall13)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteAxisGridCall14)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteAxisGridCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisGridCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteAxisGridCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteAxisGridCall21)(const void *, int *);
typedef void (*CuteAxisGridCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteAxisGridCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteAxisGridCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteAxisGridCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisGridCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteAxisGridCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteAxisGridCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteAxisGridCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteAxisGridCall33)(const void *, int *);
typedef void (*CuteAxisGridCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisGridCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisGridCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisGrid : public AxisGrid {
public:
  using AxisGrid::AxisGrid;
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

  //  void AxisGrid::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisGridCall0 call = reinterpret_cast<CuteAxisGridCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    AxisGrid::componentComplete();
  }

  //  void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF
  //      &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisGridCall1 call = reinterpret_cast<CuteAxisGridCall1>(taken[1]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    AxisGrid::geometryChange(newGeometry, oldGeometry);
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(quick_shadereffect)
  //  bool QQuickShaderEffect::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisGridCall2 call = reinterpret_cast<CuteAxisGridCall2>(taken[2]);
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
      CuteAxisGridCall3 call = reinterpret_cast<CuteAxisGridCall3>(taken[3]);
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
      CuteAxisGridCall4 call = reinterpret_cast<CuteAxisGridCall4>(taken[4]);
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
      CuteAxisGridCall5 call = reinterpret_cast<CuteAxisGridCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[6]) {
      int handled = 0;
      CuteAxisGridCall6 call = reinterpret_cast<CuteAxisGridCall6>(taken[6]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[7]) {
      int handled = 0;
      CuteAxisGridCall7 call = reinterpret_cast<CuteAxisGridCall7>(taken[7]);
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
      CuteAxisGridCall8 call = reinterpret_cast<CuteAxisGridCall8>(taken[8]);
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
      CuteAxisGridCall9 call = reinterpret_cast<CuteAxisGridCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteAxisGridCall10 call = reinterpret_cast<CuteAxisGridCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteAxisGridCall11 call = reinterpret_cast<CuteAxisGridCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteAxisGridCall12 call = reinterpret_cast<CuteAxisGridCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteAxisGridCall13 call = reinterpret_cast<CuteAxisGridCall13>(taken[13]);
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
      CuteAxisGridCall14 call = reinterpret_cast<CuteAxisGridCall14>(taken[14]);
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
      CuteAxisGridCall15 call = reinterpret_cast<CuteAxisGridCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteAxisGridCall16 call = reinterpret_cast<CuteAxisGridCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteAxisGridCall17 call = reinterpret_cast<CuteAxisGridCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteAxisGridCall18 call = reinterpret_cast<CuteAxisGridCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteAxisGridCall19 call = reinterpret_cast<CuteAxisGridCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteAxisGridCall20 call = reinterpret_cast<CuteAxisGridCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteAxisGridCall21 call = reinterpret_cast<CuteAxisGridCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteAxisGridCall22 call = reinterpret_cast<CuteAxisGridCall22>(taken[22]);
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
      CuteAxisGridCall23 call = reinterpret_cast<CuteAxisGridCall23>(taken[23]);
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
      CuteAxisGridCall24 call = reinterpret_cast<CuteAxisGridCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteAxisGridCall25 call = reinterpret_cast<CuteAxisGridCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteAxisGridCall26 call = reinterpret_cast<CuteAxisGridCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteAxisGridCall27 call = reinterpret_cast<CuteAxisGridCall27>(taken[27]);
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
      CuteAxisGridCall28 call = reinterpret_cast<CuteAxisGridCall28>(taken[28]);
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
      CuteAxisGridCall29 call = reinterpret_cast<CuteAxisGridCall29>(taken[29]);
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
      CuteAxisGridCall30 call = reinterpret_cast<CuteAxisGridCall30>(taken[30]);
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
      CuteAxisGridCall31 call = reinterpret_cast<CuteAxisGridCall31>(taken[31]);
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
      CuteAxisGridCall32 call = reinterpret_cast<CuteAxisGridCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteAxisGridCall33 call = reinterpret_cast<CuteAxisGridCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteAxisGridCall34 call = reinterpret_cast<CuteAxisGridCall34>(taken[34]);
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
      CuteAxisGridCall35 call = reinterpret_cast<CuteAxisGridCall35>(taken[35]);
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
      CuteAxisGridCall36 call = reinterpret_cast<CuteAxisGridCall36>(taken[36]);
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
      CuteAxisGridCall37 call = reinterpret_cast<CuteAxisGridCall37>(taken[37]);
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
      CuteAxisGridCall38 call = reinterpret_cast<CuteAxisGridCall38>(taken[38]);
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
      CuteAxisGridCall39 call = reinterpret_cast<CuteAxisGridCall39>(taken[39]);
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
      CuteAxisGridCall40 call = reinterpret_cast<CuteAxisGridCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisGrid::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8AxisGrid10metaObjectEv(const AxisGrid *self) {
  return self->metaObject();
}

//  void AxisGrid::setupShaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid12setupShadersEv(AxisGrid *self) {
  self->setupShaders();
}

//  QVector3D AxisGrid::iResolution() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8AxisGrid11iResolutionEv(const AxisGrid *self) {
  return new QVector3D(self->iResolution());
}

//  qreal AxisGrid::smoothing() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid9smoothingEv(const AxisGrid *self) {
  return self->smoothing();
}

//  int AxisGrid::origo() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8AxisGrid5origoEv(const AxisGrid *self) {
  return self->origo();
}

//  QVector4D AxisGrid::gridVisibility() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8AxisGrid14gridVisibilityEv(const AxisGrid *self) {
  return new QVector4D(self->gridVisibility());
}

//  qreal AxisGrid::gridWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid9gridWidthEv(const AxisGrid *self) {
  return self->gridWidth();
}

//  qreal AxisGrid::gridHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid10gridHeightEv(const AxisGrid *self) {
  return self->gridHeight();
}

//  QPointF AxisGrid::gridMovement() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8AxisGrid12gridMovementEv(const AxisGrid *self) {
  return new QPointF(self->gridMovement());
}

//  QColor AxisGrid::subGridColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisGrid12subGridColorEv(const AxisGrid *self) {
  return new QColor(self->subGridColor());
}

//  QColor AxisGrid::gridColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisGrid9gridColorEv(const AxisGrid *self) {
  return new QColor(self->gridColor());
}

//  QColor AxisGrid::plotAreaBackgroundColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK8AxisGrid23plotAreaBackgroundColorEv(
    const AxisGrid *self) {
  return new QColor(self->plotAreaBackgroundColor());
}

//  qreal AxisGrid::subGridLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid16subGridLineWidthEv(const AxisGrid *self) {
  return self->subGridLineWidth();
}

//  qreal AxisGrid::gridLineWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid13gridLineWidthEv(const AxisGrid *self) {
  return self->gridLineWidth();
}

//  qreal AxisGrid::verticalSubGridScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid20verticalSubGridScaleEv(const AxisGrid *self) {
  return self->verticalSubGridScale();
}

//  qreal AxisGrid::horizontalSubGridScale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid22horizontalSubGridScaleEv(const AxisGrid *self) {
  return self->horizontalSubGridScale();
}

//  bool AxisGrid::isVerticalLogarithmic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8AxisGrid21isVerticalLogarithmicEv(const AxisGrid *self) {
  return self->isVerticalLogarithmic();
}

//  bool AxisGrid::isHorizontalLogarithmic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8AxisGrid23isHorizontalLogarithmicEv(const AxisGrid *self) {
  return self->isHorizontalLogarithmic();
}

//  qreal AxisGrid::verticalBase() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid12verticalBaseEv(const AxisGrid *self) {
  return self->verticalBase();
}

//  qreal AxisGrid::horizontalBase() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8AxisGrid14horizontalBaseEv(const AxisGrid *self) {
  return self->horizontalBase();
}

//  void AxisGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid17componentCompleteEv(AxisGrid *self) {
  self->componentComplete();
}

//  void AxisGrid::geometryChange(const QRectF &newGeometry, const QRectF
//      &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN8AxisGrid14geometryChangeERK6QRectFS2_(
    AxisGrid *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  a Python function taken by a CuteAxisGrid, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisGrid(AxisGrid *self, const char *key, void *call) {
  return static_cast<CuteAxisGrid *>(self)->take(key, call);
}

//  void AxisGrid::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8AxisGrid17componentCompleteEv(AxisGrid *self) {
  static_cast<OwnAxisGrid *>(self)->OwnAxisGrid::componentComplete();
}

#endif  // !(!QT_CONFIG(graphs_2d_area) && !QT_CONFIG(graphs_2d_bar) && !QT_CONFIG(graphs_2d_donut_pie) && !QT_CONFIG(graphs_2d_line) && !QT_CONFIG(graphs_2d_scatter) && !QT_CONFIG(graphs_2d_spline) && !QT_CONFIG(graphs_2d_custom))
