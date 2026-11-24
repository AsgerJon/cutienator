//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativeopenglrendernode_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtChartsQml/qtchartsqmlexports.h>
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#if QT_CONFIG(opengl)
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeopenglrendernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qevent.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/private/declarativeopenglrendernode_p.h>
#include <QtGui/QOpenGLContext>
#include <QtGui/QOpenGLFunctions>
#include <QtOpenGL/QOpenGLFramebufferObjectFormat>
#include <QtOpenGL/QOpenGLFramebufferObject>
#include <QOpenGLShaderProgram>
#include <QtOpenGL/QOpenGLBuffer>
#include <QtQuick/QQuickOpenGLUtils>
#ifdef QDEBUG_TRACE_GL_FPS
#  include <QtCore/QElapsedTimer>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 55, as _ZN27DeclarativeOpenGLRenderNodeD1Ev
inline DeclarativeOpenGLRenderNode::~DeclarativeOpenGLRenderNode()
{
    cleanXYSeriesResources(0);

    delete m_texture;
    delete m_fbo;
    delete m_resolvedFbo;
    delete m_selectionFbo;
    delete m_program;

    qDeleteAll(m_mouseEvents);
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 189, as _ZN27DeclarativeOpenGLRenderNode14setTextureSizeERK5QSize
inline void DeclarativeOpenGLRenderNode::setTextureSize(const QSize &size)
{
    m_textureSize = size;
    m_recreateFbo = true;
    m_renderNeeded = true;
    m_selectionRenderNeeded = true;
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 241, as _ZN27DeclarativeOpenGLRenderNode7setRectERK6QRectF
inline void DeclarativeOpenGLRenderNode::setRect(const QRectF &rect)
{
    m_rect = rect;

    if (m_imageNode)
        m_imageNode->setRect(rect);
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 249, as _ZN27DeclarativeOpenGLRenderNode15setAntialiasingEb
inline void DeclarativeOpenGLRenderNode::setAntialiasing(bool enable)
{
    if (m_antialiasing != enable) {
        m_antialiasing = enable;
        m_recreateFbo = true;
        m_renderNeeded = true;
    }
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 258, as _ZN27DeclarativeOpenGLRenderNode14addMouseEventsERK5QListIP11QMouseEventE
inline void DeclarativeOpenGLRenderNode::addMouseEvents(const QList<QMouseEvent *> &events)
{
    if (events.size()) {
        m_mouseEvents.append(events);
        markDirty(DirtyMaterial);
    }
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 272, as _ZN27DeclarativeOpenGLRenderNode8renderGLEb
inline void DeclarativeOpenGLRenderNode::renderGL(bool selection)
{
    glClearColor(0, 0, 0, 0);

    QOpenGLVertexArrayObject::Binder vaoBinder(&m_vao);
    m_program->bind();

    glClear(GL_COLOR_BUFFER_BIT);
    glEnableVertexAttribArray(0);

    glViewport(0, 0, m_textureSize.width(), m_textureSize.height());

    int counter = 0;
    for (auto i = m_xyDataMap.begin(), end = m_xyDataMap.end(); i != end; ++i) {
        QOpenGLBuffer *vbo = m_seriesBufferMap.value(i.key());
        GLXYSeriesData *data = i.value();

        if (data->visible) {
            if (selection) {
                m_selectionList[counter] = i.key();
                m_program->setUniformValue(m_colorUniformLoc, QVector3D((counter & 0xff) / 255.0f,
                                                                        ((counter & 0xff00) >> 8) / 255.0f,
                                                                        ((counter & 0xff0000) >> 16) / 255.0f));
                counter++;
            } else {
                m_program->setUniformValue(m_colorUniformLoc, data->color);
            }
            m_program->setUniformValue(m_minUniformLoc, data->min);
            m_program->setUniformValue(m_deltaUniformLoc, data->delta);
            m_program->setUniformValue(m_matrixUniformLoc, data->matrix);

            if (!vbo) {
                vbo = new QOpenGLBuffer;
                m_seriesBufferMap.insert(i.key(), vbo);
                vbo->create();
            }
            vbo->bind();
            if (data->dirty) {
                vbo->allocate(data->array.constData(), int(data->array.size() * sizeof(GLfloat)));
                data->dirty = false;
            }

            glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, 0);
            if (data->type == QAbstractSeries::SeriesTypeLine) {
                glLineWidth(data->width);
                glDrawArrays(GL_LINE_STRIP, 0, data->array.size() / 2);
            } else { // Scatter
                m_program->setUniformValue(m_pointSizeUniformLoc, data->width);
                glDrawArrays(GL_POINTS, 0, data->array.size() / 2);
            }
            vbo->release();
        }
    }
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 327, as _ZN27DeclarativeOpenGLRenderNode15renderSelectionEv
inline void DeclarativeOpenGLRenderNode::renderSelection()
{
    m_selectionFbo->bind();

    m_selectionList.resize(m_xyDataMap.size());

    renderGL(true);

    m_selectionRenderNeeded = false;
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 338, as _ZN27DeclarativeOpenGLRenderNode12renderVisualEv
inline void DeclarativeOpenGLRenderNode::renderVisual()
{
    m_fbo->bind();

    renderGL(false);

    if (m_resolvedFbo) {
        QRect rect(QPoint(0, 0), m_fbo->size());
        QOpenGLFramebufferObject::blitFramebuffer(m_resolvedFbo, rect, m_fbo, rect);
    }

    markDirty(DirtyMaterial);

#ifdef QDEBUG_TRACE_GL_FPS
    static QElapsedTimer stopWatch;
    static int frameCount = -1;
    if (frameCount == -1) {
        stopWatch.start();
        frameCount = 0;
    }
    frameCount++;
    int elapsed = stopWatch.elapsed();
    if (elapsed >= 1000) {
        elapsed = stopWatch.restart();
        qreal fps = qreal(0.1 * int(10000.0 * (qreal(frameCount) / qreal(elapsed))));
        qDebug() << "FPS:" << fps;
        frameCount = 0;
    }
#endif
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 148, as _ZN27DeclarativeOpenGLRenderNode11recreateFBOEv
inline void DeclarativeOpenGLRenderNode::recreateFBO()
{
    QOpenGLFramebufferObjectFormat fboFormat;
    fboFormat.setAttachment(QOpenGLFramebufferObject::NoAttachment);

    int samples = 0;
    QOpenGLContext *context = QOpenGLContext::currentContext();

    if (m_antialiasing && (!context->isOpenGLES() || context->format().majorVersion() >= 3))
        samples = 4;
    fboFormat.setSamples(samples);

    delete m_fbo;
    delete m_resolvedFbo;
    delete m_selectionFbo;
    m_resolvedFbo = nullptr;

    m_fbo = new QOpenGLFramebufferObject(m_textureSize, fboFormat);
    if (samples > 0)
        m_resolvedFbo = new QOpenGLFramebufferObject(m_textureSize);
    m_selectionFbo = new QOpenGLFramebufferObject(m_textureSize);

    delete m_texture;
    uint textureId = m_resolvedFbo ? m_resolvedFbo->texture() : m_fbo->texture();
    m_texture = QNativeInterface::QSGOpenGLTexture::fromNative(textureId, m_window, m_textureSize, m_textureOptions);

    if (!m_imageNode) {
        m_imageNode = m_window->createImageNode();
        m_imageNode->setFiltering(QSGTexture::Linear);
        m_imageNode->setTextureCoordinatesTransform(QSGImageNode::MirrorVertically);
        m_imageNode->setFlag(OwnedByParent);
        if (!m_rect.isEmpty())
            m_imageNode->setRect(m_rect);
        appendChildNode(m_imageNode);
    }
    m_imageNode->setTexture(m_texture);

    m_recreateFbo = false;
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 397, as _ZN27DeclarativeOpenGLRenderNode22cleanXYSeriesResourcesEPK9QXYSeries
inline void DeclarativeOpenGLRenderNode::cleanXYSeriesResources(const QXYSeries *series)
{
    if (series) {
        delete m_seriesBufferMap.take(series);
        delete m_xyDataMap.take(series);
    } else {
        for (QOpenGLBuffer *buffer : std::as_const(m_seriesBufferMap))
            delete buffer;
        m_seriesBufferMap.clear();
        for (GLXYSeriesData *data : std::as_const(m_xyDataMap))
            delete data;
        m_xyDataMap.clear();
    }
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 412, as _ZN27DeclarativeOpenGLRenderNode17handleMouseEventsEv
inline void DeclarativeOpenGLRenderNode::handleMouseEvents()
{
    if (m_mouseEvents.size()) {
        if (m_xyDataMap.size()) {
            if (m_selectionRenderNeeded)
                renderSelection();
        }
        for (const QMouseEvent *event : std::as_const(m_mouseEvents)) {
            const QXYSeries *series = findSeriesAtEvent(event);
            switch (event->type()) {
            case QEvent::MouseMove: {
                if (series != m_lastHoverSeries) {
                    if (m_lastHoverSeries) {
                        m_mouseEventResponses.append(
                                    MouseEventResponse(MouseEventResponse::HoverLeave,
                                                       event->pos(), m_lastHoverSeries));
                    }
                    if (series) {
                        m_mouseEventResponses.append(
                                    MouseEventResponse(MouseEventResponse::HoverEnter,
                                                       event->pos(), series));
                    }
                    m_lastHoverSeries = series;
                }
                break;
            }
            case QEvent::MouseButtonPress: {
                if (series) {
                    m_mousePressed = true;
                    m_mousePressPos = event->pos();
                    m_lastPressSeries = series;
                    m_mouseEventResponses.append(
                                MouseEventResponse(MouseEventResponse::Pressed,
                                                   event->pos(), series));
                }
                break;
            }
            case QEvent::MouseButtonRelease: {
                m_mouseEventResponses.append(
                            MouseEventResponse(MouseEventResponse::Released,
                                               m_mousePressPos, m_lastPressSeries));
                if (m_mousePressed) {
                    m_mouseEventResponses.append(
                                MouseEventResponse(MouseEventResponse::Clicked,
                                                   m_mousePressPos, m_lastPressSeries));
                }
                if (m_lastHoverSeries == m_lastPressSeries && m_lastHoverSeries != series) {
                    if (m_lastHoverSeries) {
                        m_mouseEventResponses.append(
                                    MouseEventResponse(MouseEventResponse::HoverLeave,
                                                       event->pos(), m_lastHoverSeries));
                    }
                    m_lastHoverSeries = nullptr;
                }
                m_lastPressSeries = nullptr;
                m_mousePressed = false;
                break;
            }
            case QEvent::MouseButtonDblClick: {
                if (series) {
                    m_mouseEventResponses.append(
                                MouseEventResponse(MouseEventResponse::DoubleClicked,
                                                   event->pos(), series));
                }
                break;
            }
            default:
                break;
            }
        }

        qDeleteAll(m_mouseEvents);
        m_mouseEvents.clear();
    }
}

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 488, as _ZN27DeclarativeOpenGLRenderNode17findSeriesAtEventEPK11QMouseEvent
inline const QXYSeries *DeclarativeOpenGLRenderNode::findSeriesAtEvent(const QMouseEvent *event)
{
    const QXYSeries *series = nullptr;
    int index = -1;

    if (m_xyDataMap.size()) {
        m_selectionFbo->bind();

        GLubyte pixel[4] = {0, 0, 0, 0};
        glReadPixels(event->pos().x(), m_textureSize.height() - event->pos().y(),
                     1, 1, GL_RGBA, GL_UNSIGNED_BYTE,
                     (void *)pixel);
        if (pixel[3] == 0xff)
            index = pixel[0] + (pixel[1] << 8) + (pixel[2] << 16);
    }

    if (index >= 0 && index < m_selectionList.size())
        series = m_selectionList.at(index);

    return series;
}
//  -----------------------------------------------------------------------

//  A DeclarativeOpenGLRenderNode that Python can take functions over in. Every DeclarativeOpenGLRenderNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QSize * (*CuteDeclarativeOpenGLRenderNodeCall0)(const void *, int *);
typedef void (*CuteDeclarativeOpenGLRenderNodeCall1)(const void *, const QSize *, int *);
typedef void (*CuteDeclarativeOpenGLRenderNodeCall2)(const void *, const QRectF *, int *);
typedef void (*CuteDeclarativeOpenGLRenderNodeCall3)(const void *, bool, int *);
typedef bool (*CuteDeclarativeOpenGLRenderNodeCall4)(const void *, int *);
typedef void (*CuteDeclarativeOpenGLRenderNodeCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeOpenGLRenderNodeCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteDeclarativeOpenGLRenderNodeCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeOpenGLRenderNodeCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeOpenGLRenderNodeCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeOpenGLRenderNodeCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeOpenGLRenderNodeCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteDeclarativeOpenGLRenderNodeCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteDeclarativeOpenGLRenderNode : public DeclarativeOpenGLRenderNode {
public:
  using DeclarativeOpenGLRenderNode::DeclarativeOpenGLRenderNode;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK29DeclarativeAbstractRenderNode11textureSizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29DeclarativeAbstractRenderNode14setTextureSizeERK5QSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29DeclarativeAbstractRenderNode7setRectERK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29DeclarativeAbstractRenderNode15setAntialiasingEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSize DeclarativeOpenGLRenderNode::textureSize() const
  QSize textureSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall0 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall0>(taken[0]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return DeclarativeOpenGLRenderNode::textureSize();
  }

  //  void DeclarativeOpenGLRenderNode::setTextureSize(const QSize &size)
  void setTextureSize(const QSize &size) override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall1 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall1>(taken[1]);
      call(this, &size, &handled);
      if (handled) return;
    }
    DeclarativeOpenGLRenderNode::setTextureSize(size);
  }

  //  void DeclarativeOpenGLRenderNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall2 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
    DeclarativeOpenGLRenderNode::setRect(rect);
  }

  //  void DeclarativeOpenGLRenderNode::setAntialiasing(bool enable)
  void setAntialiasing(bool enable) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall3 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall3>(taken[3]);
      call(this, enable, &handled);
      if (handled) return;
    }
    DeclarativeOpenGLRenderNode::setAntialiasing(enable);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[4]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall4 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[5]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall5 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall6 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall7 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall8 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall9 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall10 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall11 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteDeclarativeOpenGLRenderNodeCall12 call = reinterpret_cast<CuteDeclarativeOpenGLRenderNodeCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *DeclarativeOpenGLRenderNode::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27DeclarativeOpenGLRenderNode10metaObjectEv(
    const DeclarativeOpenGLRenderNode *self) {
  return self->metaObject();
}

//  DeclarativeOpenGLRenderNode::~DeclarativeOpenGLRenderNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNodeD1Ev(
    DeclarativeOpenGLRenderNode *self) {
  delete self;
}

//  QSize DeclarativeOpenGLRenderNode::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK27DeclarativeOpenGLRenderNode11textureSizeEv(
    const DeclarativeOpenGLRenderNode *self) {
  return new QSize(self->textureSize());
}

//  void DeclarativeOpenGLRenderNode::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode14setTextureSizeERK5QSize(
    DeclarativeOpenGLRenderNode *self,
    const QSize *size) {
  self->setTextureSize(*size);
}

//  void DeclarativeOpenGLRenderNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode7setRectERK6QRectF(
    DeclarativeOpenGLRenderNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void DeclarativeOpenGLRenderNode::setAntialiasing(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode15setAntialiasingEb(
    DeclarativeOpenGLRenderNode *self,
    bool enable) {
  self->setAntialiasing(enable);
}

//  void DeclarativeOpenGLRenderNode::addMouseEvents(const QList<QMouseEvent
//      *> &events)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode14addMouseEventsERK5QListIP11QMouseEventE(
    DeclarativeOpenGLRenderNode *self,
    const QList<QMouseEvent *> *events) {
  self->addMouseEvents(*events);
}

//  void DeclarativeOpenGLRenderNode::renderGL(bool selection)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode8renderGLEb(
    DeclarativeOpenGLRenderNode *self,
    bool selection) {
  self->renderGL(selection);
}

//  void DeclarativeOpenGLRenderNode::renderSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode15renderSelectionEv(
    DeclarativeOpenGLRenderNode *self) {
  self->renderSelection();
}

//  void DeclarativeOpenGLRenderNode::renderVisual()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode12renderVisualEv(
    DeclarativeOpenGLRenderNode *self) {
  self->renderVisual();
}

//  void DeclarativeOpenGLRenderNode::recreateFBO()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode11recreateFBOEv(
    DeclarativeOpenGLRenderNode *self) {
  self->recreateFBO();
}

//  void DeclarativeOpenGLRenderNode::cleanXYSeriesResources(const QXYSeries
//      *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode22cleanXYSeriesResourcesEPK9QXYSeries(
    DeclarativeOpenGLRenderNode *self,
    const QXYSeries *series) {
  self->cleanXYSeriesResources(series);
}

//  void DeclarativeOpenGLRenderNode::handleMouseEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN27DeclarativeOpenGLRenderNode17handleMouseEventsEv(
    DeclarativeOpenGLRenderNode *self) {
  self->handleMouseEvents();
}

//  const QXYSeries *DeclarativeOpenGLRenderNode::findSeriesAtEvent(const
//      QMouseEvent *event)
extern "C" Q_DECL_EXPORT
const QXYSeries *ritual_ZN27DeclarativeOpenGLRenderNode17findSeriesAtEventEPK11QMouseEvent(
    DeclarativeOpenGLRenderNode *self,
    const QMouseEvent *event) {
  return self->findSeriesAtEvent(event);
}

//  DeclarativeOpenGLRenderNode as the DeclarativeAbstractRenderNode it is
//      built on
extern "C" Q_DECL_EXPORT
DeclarativeAbstractRenderNode *ritual_cast_DeclarativeOpenGLRenderNode_DeclarativeAbstractRenderNode(
    DeclarativeOpenGLRenderNode *self) {
  return static_cast<DeclarativeAbstractRenderNode *>(self);
}

//  DeclarativeOpenGLRenderNode as the QOpenGLFunctions it is built on
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_cast_DeclarativeOpenGLRenderNode_QOpenGLFunctions(
    DeclarativeOpenGLRenderNode *self) {
  return static_cast<QOpenGLFunctions *>(self);
}

//  a Python function taken by a CuteDeclarativeOpenGLRenderNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeOpenGLRenderNode(
    DeclarativeOpenGLRenderNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeOpenGLRenderNode *>(self)->take(key, call);
}

//  QSize DeclarativeOpenGLRenderNode::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK27DeclarativeOpenGLRenderNode11textureSizeEv(
    const DeclarativeOpenGLRenderNode *self) {
  return new QSize(self->DeclarativeOpenGLRenderNode::textureSize());
}

//  void DeclarativeOpenGLRenderNode::setTextureSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativeOpenGLRenderNode14setTextureSizeERK5QSize(
    DeclarativeOpenGLRenderNode *self,
    const QSize *size) {
  self->DeclarativeOpenGLRenderNode::setTextureSize(*size);
}

//  void DeclarativeOpenGLRenderNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativeOpenGLRenderNode7setRectERK6QRectF(
    DeclarativeOpenGLRenderNode *self,
    const QRectF *rect) {
  self->DeclarativeOpenGLRenderNode::setRect(*rect);
}

//  void DeclarativeOpenGLRenderNode::setAntialiasing(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27DeclarativeOpenGLRenderNode15setAntialiasingEb(
    DeclarativeOpenGLRenderNode *self,
    bool enable) {
  self->DeclarativeOpenGLRenderNode::setAntialiasing(enable);
}

#endif  // QT_CONFIG(opengl)
