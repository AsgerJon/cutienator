//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativechartnode_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qrect.h>
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
#include <QtChartsQml/private/declarativechartnode_p.h>
#include <QtChartsQml/private/declarativeabstractrendernode_p.h>
#include <QtQuick/QQuickWindow>
#include <QtQuick/QSGImageNode>
#include <QtQuick/QSGRendererInterface>
#ifndef QT_NO_OPENGL
# include <QtChartsQml/private/declarativeopenglrendernode_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/chartsqml2/declarativeopenglrendernode.cpp, line 25, as _ZN27DeclarativeOpenGLRenderNodeC1EP12QQuickWindow
inline DeclarativeOpenGLRenderNode::DeclarativeOpenGLRenderNode(QQuickWindow *window) :
    QObject(),
    m_texture(nullptr),
    m_imageNode(nullptr),
    m_window(window),
    m_textureOptions(QQuickWindow::TextureHasAlphaChannel),
    m_textureSize(1, 1),
    m_recreateFbo(false),
    m_fbo(nullptr),
    m_resolvedFbo(nullptr),
    m_selectionFbo(nullptr),
    m_program(nullptr),
    m_shaderAttribLoc(-1),
    m_colorUniformLoc(-1),
    m_minUniformLoc(-1),
    m_deltaUniformLoc(-1),
    m_pointSizeUniformLoc(-1),
    m_renderNeeded(true),
    m_antialiasing(false),
    m_selectionRenderNeeded(true),
    m_mousePressed(false),
    m_lastPressSeries(nullptr),
    m_lastHoverSeries(nullptr)
{
    initializeOpenGLFunctions();

    connect(m_window, &QQuickWindow::beforeRendering,
            this, &DeclarativeOpenGLRenderNode::render);
}

//  from ../qtcharts/src/chartsqml2/declarativechartnode.cpp, line 37, as _ZN20DeclarativeChartNodeD1Ev
inline DeclarativeChartNode::~DeclarativeChartNode()
{
}

//  from ../qtcharts/src/chartsqml2/declarativechartnode.cpp, line 42, as _ZN20DeclarativeChartNode22createTextureFromImageERK6QImage
inline void DeclarativeChartNode::createTextureFromImage(const QImage &chartImage)
{
    static auto const defaultTextureOptions = QQuickWindow::CreateTextureOptions(QQuickWindow::TextureHasAlphaChannel |
                                                                                 QQuickWindow::TextureOwnsGLTexture);

    auto texture = m_window->createTextureFromImage(chartImage, defaultTextureOptions);
    // Create Image node if needed
    if (!m_imageNode) {
        m_imageNode = m_window->createImageNode();
        m_imageNode->setFlag(OwnedByParent);
        m_imageNode->setOwnsTexture(true);
        m_imageNode->setTexture(texture);
        prependChildNode(m_imageNode);
    } else {
        m_imageNode->setTexture(texture);
    }
    if (!m_rect.isEmpty())
        m_imageNode->setRect(m_rect);
}

//  from ../qtcharts/src/chartsqml2/declarativechartnode.cpp, line 62, as _ZN20DeclarativeChartNode7setRectERK6QRectF
inline void DeclarativeChartNode::setRect(const QRectF &rect)
{
    m_rect = rect;

    if (m_imageNode)
        m_imageNode->setRect(rect);
}
//  -----------------------------------------------------------------------

//  A DeclarativeChartNode that Python can take functions over in. Every DeclarativeChartNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteDeclarativeChartNodeCall0)(const void *, int *);
typedef void (*CuteDeclarativeChartNodeCall1)(const void *, int *);
class CuteDeclarativeChartNode : public DeclarativeChartNode {
public:
  using DeclarativeChartNode::DeclarativeChartNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeChartNodeCall0 call = reinterpret_cast<CuteDeclarativeChartNodeCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeChartNodeCall1 call = reinterpret_cast<CuteDeclarativeChartNodeCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  DeclarativeChartNode::~DeclarativeChartNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeChartNodeD1Ev(DeclarativeChartNode *self) {
  delete self;
}

//  void DeclarativeChartNode::createTextureFromImage(const QImage
//      &chartImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeChartNode22createTextureFromImageERK6QImage(
    DeclarativeChartNode *self,
    const QImage *chartImage) {
  self->createTextureFromImage(*chartImage);
}

//  DeclarativeAbstractRenderNode *DeclarativeChartNode::renderNode() const
extern "C" Q_DECL_EXPORT
DeclarativeAbstractRenderNode *ritual_ZNK20DeclarativeChartNode10renderNodeEv(
    const DeclarativeChartNode *self) {
  return self->renderNode();
}

//  void DeclarativeChartNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN20DeclarativeChartNode7setRectERK6QRectF(
    DeclarativeChartNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  a Python function taken by a CuteDeclarativeChartNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeChartNode(
    DeclarativeChartNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeChartNode *>(self)->take(key, call);
}
