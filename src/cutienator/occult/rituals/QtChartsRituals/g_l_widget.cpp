//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/glwidget_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'GLWidget' is pasted in,
//  cut from what the moc of Qt 6.12.0 writes for its header: Qt's library
//  keeps it to itself; added are 3 rituals that lean on what moc writes for
//  a class of the part Qt keeps to itself, whose ritual file carries moc's
//  output, drafted by a copy of the generator that lets those names through.
//  A copy of a meta-object is a second one: 'qobject_cast' between it and
//  Qt's own does not match. Kept as it is when the generator runs again.
#include <QtGui/qtguiglobal.h>
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(opengl)
#if !defined(QT_NO_OPENGL)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/glwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#ifndef QT_NO_OPENGL
#include <QtCharts/private/glwidget_p.h>
#include <QtCharts/private/glxyseriesdata_p.h>
#include <QtCharts/private/qabstractseries_p.h>
#include <QtOpenGL/QOpenGLShaderProgram>
#include <QtGui/QOpenGLContext>
#include <QtOpenGL/QOpenGLBuffer>
#ifdef QDEBUG_TRACE_GL_FPS
#  include <QtCore/QElapsedTimer>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcharts/src/charts/glwidget.cpp, line 99, as local:glwidget.cpp:vertexSource
#if !defined(QT_NO_OPENGL)
static const char *vertexSource =
        "attribute highp vec2 points;\n"
        "uniform highp vec2 min;\n"
        "uniform highp vec2 delta;\n"
        "uniform highp float pointSize;\n"
        "uniform highp mat4 matrix;\n"
        "void main() {\n"
        "  vec2 normalPoint = vec2(-1, -1) + ((points - min) / delta);\n"
        "  gl_Position = matrix * vec4(normalPoint, 0, 1);\n"
        "  gl_PointSize = pointSize;\n"
        "}";
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 110, as local:glwidget.cpp:fragmentSource
#if !defined(QT_NO_OPENGL)
static const char *fragmentSource =
        "uniform highp vec3 color;\n"
        "void main() {\n"
        "  gl_FragColor = vec4(color,1);\n"
        "}\n";
#endif  // !defined(QT_NO_OPENGL)

//  from QtCharts__GLWidget.cpp, line 1, as moc:GLWidget
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN8GLWidgetE_t {};
} // unnamed namespace

template <> constexpr inline auto GLWidget::qt_create_metaobjectdata<qt_meta_tag_ZN8GLWidgetE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "GLWidget",
        "cleanup",
        "",
        "cleanXYSeriesResources",
        "const QXYSeries*",
        "series"
    };

    QtMocHelpers::UintData qt_methods {
        // Slot 'cleanup'
        QtMocHelpers::SlotData<void()>(1, 2, QMC::AccessPublic, QMetaType::Void),
        // Slot 'cleanXYSeriesResources'
        QtMocHelpers::SlotData<void(const QXYSeries *)>(3, 2, QMC::AccessPublic, QMetaType::Void, {{
            { 0x80000000 | 4, 5 },
        }}),
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<GLWidget, qt_meta_tag_ZN8GLWidgetE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject GLWidget::staticMetaObject = { {
    QMetaObject::SuperData::link<QOpenGLWidget::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8GLWidgetE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8GLWidgetE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN8GLWidgetE_t>.metaTypes,
    nullptr
} };

void GLWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<GLWidget *>(_o);
    if (_c == QMetaObject::InvokeMetaMethod) {
        switch (_id) {
        case 0: _t->cleanup(); break;
        case 1: _t->cleanXYSeriesResources((*reinterpret_cast<std::add_pointer_t<const QXYSeries*>>(_a[1]))); break;
        default: ;
        }
    }
}

const QMetaObject *GLWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *GLWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN8GLWidgetE_t>.strings))
        return static_cast<void*>(this);
    if (!strcmp(_clname, "QOpenGLFunctions"))
        return static_cast< QOpenGLFunctions*>(this);
    return QOpenGLWidget::qt_metacast(_clname);
}

int GLWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QOpenGLWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 2)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 2;
    }
    if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 2)
            *reinterpret_cast<QMetaType *>(_a[0]) = QMetaType();
        _id -= 2;
    }
    return _id;
}
QT_WARNING_POP

//  from ../qtcharts/src/charts/glwidget.cpp, line 116, as _ZN8GLWidget12initializeGLEv
#if !defined(QT_NO_OPENGL)
inline void GLWidget::initializeGL()
{
    connect(context(), &QOpenGLContext::aboutToBeDestroyed, this, &GLWidget::cleanup);

    initializeOpenGLFunctions();
    glClearColor(0, 0, 0, 0);

    m_program = new QOpenGLShaderProgram;
    m_program->addShaderFromSourceCode(QOpenGLShader::Vertex, vertexSource);
    m_program->addShaderFromSourceCode(QOpenGLShader::Fragment, fragmentSource);
    m_program->bindAttributeLocation("points", 0);
    m_program->link();

    m_program->bind();
    m_colorUniformLoc = m_program->uniformLocation("color");
    m_minUniformLoc = m_program->uniformLocation("min");
    m_deltaUniformLoc = m_program->uniformLocation("delta");
    m_pointSizeUniformLoc = m_program->uniformLocation("pointSize");
    m_matrixUniformLoc = m_program->uniformLocation("matrix");


    // Create a vertex array object. In OpenGL ES 2.0 and OpenGL 2.x
    // implementations this is optional and support may not be present
    // at all. Nonetheless the below code works in all cases and makes
    // sure there is a VAO when one is needed.
    m_vao.create();
    QOpenGLVertexArrayObject::Binder vaoBinder(&m_vao);

    glEnableVertexAttribArray(0);

    glDisable(GL_DEPTH_TEST);
    glDisable(GL_STENCIL_TEST);

#if !QT_CONFIG(opengles2)
    if (!QOpenGLContext::currentContext()->isOpenGLES()) {
        // Make it possible to change point primitive size and use textures with them in
        // the shaders. These are implicitly enabled in ES2.
        glEnable(GL_PROGRAM_POINT_SIZE);
    }
#endif

    m_program->release();
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 197, as _ZN8GLWidget14mouseMoveEventEP11QMouseEvent
#if !defined(QT_NO_OPENGL)
inline void GLWidget::mouseMoveEvent(QMouseEvent *event)
{
    if (m_view->hasMouseTracking() && !event->buttons()) {
        QXYSeries *series = findSeriesAtEvent(event);
        if (series != m_lastHoverSeries) {
            if (m_lastHoverSeries) {
                if (chartSeries(m_lastHoverSeries)) {
                    emit m_lastHoverSeries->hovered(
                                m_lastHoverSeries->d_ptr->domain()->calculateDomainPoint(
                                    event->pos()), false);
                }
            }
            if (series) {
                emit series->hovered(
                            series->d_ptr->domain()->calculateDomainPoint(event->pos()), true);
            }
            m_lastHoverSeries = series;
        }
    } else {
        event->ignore();
    }
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 220, as _ZN8GLWidget15mousePressEventEP11QMouseEvent
#if !defined(QT_NO_OPENGL)
inline void GLWidget::mousePressEvent(QMouseEvent *event)
{
    QXYSeries *series = findSeriesAtEvent(event);
    if (series) {
        m_mousePressed = true;
        m_mousePressPos = event->pos();
        m_lastPressSeries = series;
        emit series->pressed(series->d_ptr->domain()->calculateDomainPoint(event->pos()));
    }
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 231, as _ZN8GLWidget17mouseReleaseEventEP11QMouseEvent
#if !defined(QT_NO_OPENGL)
inline void GLWidget::mouseReleaseEvent(QMouseEvent *event)
{
    if (chartSeries(m_lastPressSeries)) {
        emit m_lastPressSeries->released(
                    m_lastPressSeries->d_ptr->domain()->calculateDomainPoint(m_mousePressPos));
        if (m_mousePressed) {
            emit m_lastPressSeries->clicked(
                        m_lastPressSeries->d_ptr->domain()->calculateDomainPoint(m_mousePressPos));
        }
        if (m_lastHoverSeries == m_lastPressSeries
                && m_lastHoverSeries != findSeriesAtEvent(event)) {
            if (chartSeries(m_lastHoverSeries)) {
                emit m_lastHoverSeries->hovered(
                            m_lastHoverSeries->d_ptr->domain()->calculateDomainPoint(
                                event->pos()), false);
            }
            m_lastHoverSeries = nullptr;
        }
        m_lastPressSeries = nullptr;
        m_mousePressed = false;
    } else {
        event->ignore();
    }
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 190, as _ZN8GLWidget21mouseDoubleClickEventEP11QMouseEvent
#if !defined(QT_NO_OPENGL)
inline void GLWidget::mouseDoubleClickEvent(QMouseEvent *event)
{
    QXYSeries *series = findSeriesAtEvent(event);
    if (series)
        emit series->doubleClicked(series->d_ptr->domain()->calculateDomainPoint(event->pos()));
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 85, as _ZN8GLWidget22cleanXYSeriesResourcesEPK9QXYSeries
#if !defined(QT_NO_OPENGL)
inline void GLWidget::cleanXYSeriesResources(const QXYSeries *series)
{
    makeCurrent();
    if (series) {
        delete m_seriesBufferMap.take(series);
    } else {
        // Null series means all series were removed
        for (auto buffer : std::as_const(m_seriesBufferMap))
            delete buffer;
        m_seriesBufferMap.clear();
    }
    doneCurrent();
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 68, as _ZN8GLWidget7cleanupEv
#if !defined(QT_NO_OPENGL)
inline void GLWidget::cleanup()
{
    makeCurrent();

    delete m_program;
    m_program = 0;

    for (auto buffer : std::as_const(m_seriesBufferMap))
        delete buffer;
    m_seriesBufferMap.clear();

    doneCurrent();

    if (context())
        context()->disconnect(this);
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 160, as _ZN8GLWidget7paintGLEv
#if !defined(QT_NO_OPENGL)
inline void GLWidget::paintGL()
{
    render(false);

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
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 182, as _ZN8GLWidget8resizeGLEii
#if !defined(QT_NO_OPENGL)
inline void GLWidget::resizeGL(int w, int h)
{
    m_fboSize.setWidth(w);
    m_fboSize.setHeight(h);
    m_recreateSelectionFbo = true;
    m_selectionRenderNeeded = true;
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 22, as _ZN8GLWidgetC1EP21GLXYSeriesDataManagerP6QChartP13QGraphicsView
#if !defined(QT_NO_OPENGL)
inline GLWidget::GLWidget(GLXYSeriesDataManager *xyDataManager, QChart *chart,
                   QGraphicsView *parent)
    : QOpenGLWidget(parent->viewport()),
      m_program(nullptr),
      m_shaderAttribLoc(-1),
      m_colorUniformLoc(-1),
      m_minUniformLoc(-1),
      m_deltaUniformLoc(-1),
      m_pointSizeUniformLoc(-1),
      m_xyDataManager(xyDataManager),
      m_antiAlias(parent->renderHints().testFlag(QPainter::Antialiasing)),
      m_view(parent),
      m_selectionFbo(nullptr),
      m_chart(chart),
      m_recreateSelectionFbo(true),
      m_selectionRenderNeeded(true),
      m_mousePressed(false),
      m_lastPressSeries(nullptr),
      m_lastHoverSeries(nullptr)
{
    setAttribute(Qt::WA_TranslucentBackground);
    setAttribute(Qt::WA_AlwaysStackOnTop);

    QSurfaceFormat surfaceFormat;
    surfaceFormat.setDepthBufferSize(0);
    surfaceFormat.setStencilBufferSize(0);
    surfaceFormat.setRedBufferSize(8);
    surfaceFormat.setGreenBufferSize(8);
    surfaceFormat.setBlueBufferSize(8);
    surfaceFormat.setAlphaBufferSize(8);
    surfaceFormat.setSwapBehavior(QSurfaceFormat::DoubleBuffer);
    surfaceFormat.setRenderableType(QSurfaceFormat::DefaultRenderableType);
    surfaceFormat.setSamples(m_antiAlias ? 4 : 0);
    setFormat(surfaceFormat);

    connect(xyDataManager, &GLXYSeriesDataManager::seriesRemoved,
            this, &GLWidget::cleanXYSeriesResources);

    setMouseTracking(true);
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 63, as _ZN8GLWidgetD1Ev
#if !defined(QT_NO_OPENGL)
inline GLWidget::~GLWidget()
{
    cleanup();
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 386, as _ZNK8GLWidget10needsResetEv
#if !defined(QT_NO_OPENGL)
inline bool GLWidget::needsReset() const
{
    return m_view->renderHints().testFlag(QPainter::Antialiasing) != m_antiAlias;
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 256, as _ZN8GLWidget17findSeriesAtEventEP11QMouseEvent
#if !defined(QT_NO_OPENGL)
inline QXYSeries *GLWidget::findSeriesAtEvent(QMouseEvent *event)
{
    QXYSeries *series = nullptr;
    int index = -1;

    if (m_xyDataManager->dataMap().size()) {
        makeCurrent();

        if (m_recreateSelectionFbo)
            recreateSelectionFbo();

        m_selectionFbo->bind();

        if (m_selectionRenderNeeded) {
            m_selectionList.resize(m_xyDataManager->dataMap().size());
            render(true);
            m_selectionRenderNeeded = false;
        }

        GLubyte pixel[4] = {0, 0, 0, 0};
        glReadPixels(event->pos().x(), m_fboSize.height() - event->pos().y(),
                     1, 1, GL_RGBA, GL_UNSIGNED_BYTE,
                     (void *)pixel);
        if (pixel[3] == 0xff)
            index = pixel[0] + (pixel[1] << 8) + (pixel[2] << 16);

        glBindFramebuffer(GL_FRAMEBUFFER, defaultFramebufferObject());

        doneCurrent();
    }

    if (index >= 0) {
        const QXYSeries *cSeries = nullptr;
        if (index < m_selectionList.size())
            cSeries = m_selectionList.at(index);

        series = chartSeries(cSeries);
    }
    if (series)
        event->accept();
    else
        event->ignore();

    return series;
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 302, as _ZN8GLWidget6renderEb
#if !defined(QT_NO_OPENGL)
inline void GLWidget::render(bool selection)
{
    glClear(GL_COLOR_BUFFER_BIT);

    QOpenGLVertexArrayObject::Binder vaoBinder(&m_vao);
    m_program->bind();

    int counter = 0;
    const auto &dataMap = m_xyDataManager->dataMap();
    for (auto i = dataMap.begin(), end = dataMap.end(); i != end; ++i) {
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
            bool dirty = data->dirty;
            if (!vbo) {
                vbo = new QOpenGLBuffer;
                m_seriesBufferMap.insert(i.key(), vbo);
                vbo->create();
                dirty = true;
            }
            vbo->bind();
            if (dirty) {
                vbo->allocate(data->array.constData(), int(data->array.size() * sizeof(GLfloat)));
                dirty = false;
                m_selectionRenderNeeded = true;
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
    m_program->release();
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 356, as _ZN8GLWidget20recreateSelectionFboEv
#if !defined(QT_NO_OPENGL)
inline void GLWidget::recreateSelectionFbo()
{
    QOpenGLFramebufferObjectFormat fboFormat;
    fboFormat.setAttachment(QOpenGLFramebufferObject::NoAttachment);

    delete m_selectionFbo;

    const QSize deviceSize = m_fboSize * devicePixelRatio();
    m_selectionFbo = new QOpenGLFramebufferObject(deviceSize, fboFormat);
    m_recreateSelectionFbo = false;
    m_selectionRenderNeeded = true;
}
#endif  // !defined(QT_NO_OPENGL)

//  from ../qtcharts/src/charts/glwidget.cpp, line 371, as _ZN8GLWidget11chartSeriesEPK9QXYSeries
#if !defined(QT_NO_OPENGL)
inline QXYSeries *GLWidget::chartSeries(const QXYSeries *cSeries)
{
    QXYSeries *series = nullptr;
    if (cSeries) {
        const auto allSeries = m_chart->series();
        for (QAbstractSeries *chartSeries : allSeries) {
            if (cSeries == chartSeries) {
                series = qobject_cast<QXYSeries *>(chartSeries);
                break;
            }
        }
    }
    return series;
}
#endif  // !defined(QT_NO_OPENGL)
//  -----------------------------------------------------------------------

//  Only a class built on GLWidget may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnGLWidget : GLWidget {
  using GLWidget::initializeGL;
  using GLWidget::paintGL;
  using GLWidget::resizeGL;
  using GLWidget::mouseDoubleClickEvent;
  using GLWidget::mouseMoveEvent;
  using GLWidget::mousePressEvent;
  using GLWidget::mouseReleaseEvent;
};

//  A GLWidget that Python can take functions over in. Every GLWidget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall0)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall1)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall2)(const void *, int, int, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall3)(const void *, QMouseEvent *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall4)(const void *, QMouseEvent *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall5)(const void *, QMouseEvent *, int *);
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall6)(const void *, QMouseEvent *, int *);
#endif  // !defined(QT_NO_OPENGL)
typedef void (*CuteGLWidgetCall7)(const void *, QPaintEvent *, int *);
typedef void (*CuteGLWidgetCall8)(const void *, QResizeEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteGLWidgetCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef int (*CuteGLWidgetCall10)(const void *, int, int *);
typedef void * (*CuteGLWidgetCall11)(const void *, QPoint *, int *);
typedef void * (*CuteGLWidgetCall12)(const void *, int *);
typedef int (*CuteGLWidgetCall13)(const void *, int *);
typedef void (*CuteGLWidgetCall14)(const void *, bool, int *);
typedef const QSize * (*CuteGLWidgetCall15)(const void *, int *);
typedef const QSize * (*CuteGLWidgetCall16)(const void *, int *);
typedef int (*CuteGLWidgetCall17)(const void *, int, int *);
typedef bool (*CuteGLWidgetCall18)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteGLWidgetCall19)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteGLWidgetCall20)(const void *, QKeyEvent *, int *);
typedef void (*CuteGLWidgetCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteGLWidgetCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteGLWidgetCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteGLWidgetCall24)(const void *, QEnterEvent *, int *);
typedef void (*CuteGLWidgetCall25)(const void *, QEvent *, int *);
typedef void (*CuteGLWidgetCall26)(const void *, QMoveEvent *, int *);
typedef void (*CuteGLWidgetCall27)(const void *, QCloseEvent *, int *);
#if !defined(QT_NO_CONTEXTMENU)
typedef void (*CuteGLWidgetCall28)(const void *, QContextMenuEvent *, int *);
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
typedef void (*CuteGLWidgetCall29)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
typedef void (*CuteGLWidgetCall30)(const void *, QActionEvent *, int *);
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
typedef void (*CuteGLWidgetCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteGLWidgetCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteGLWidgetCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
typedef void (*CuteGLWidgetCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void (*CuteGLWidgetCall35)(const void *, QShowEvent *, int *);
typedef void (*CuteGLWidgetCall36)(const void *, QHideEvent *, int *);
typedef void (*CuteGLWidgetCall37)(const void *, QEvent *, int *);
typedef void (*CuteGLWidgetCall38)(const void *, QPainter *, int *);
typedef void * (*CuteGLWidgetCall39)(const void *, int *);
typedef void (*CuteGLWidgetCall40)(const void *, QInputMethodEvent *, int *);
typedef const QVariant * (*CuteGLWidgetCall41)(const void *, int, int *);
typedef bool (*CuteGLWidgetCall42)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteGLWidgetCall43)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLWidgetCall44)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLWidgetCall45)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLWidgetCall46)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLWidgetCall47)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteGLWidgetCall48)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteGLWidget : public GLWidget {
public:
  using GLWidget::GLWidget;
  void *taken[49] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWidget12initializeGLEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWidget7paintGLEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN13QOpenGLWidget8resizeGLEii")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWidget21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWidget14mouseMoveEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWidget15mousePressEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWidget17mouseReleaseEventEP11QMouseEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN7QWidget10paintEventEP11QPaintEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11resizeEventEP12QResizeEvent")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget8sizeHintEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget15minimumSizeHintEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget14heightForWidthEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget17hasHeightForWidthEv")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget10wheelEventEP11QWheelEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWidget13keyPressEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget15keyReleaseEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget12focusInEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget13focusOutEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10enterEventEP11QEnterEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10leaveEventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9moveEventEP10QMoveEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget10closeEventEP11QCloseEvent")) {
      taken[27] = call;
      return true;
    }
#if !defined(QT_NO_CONTEXTMENU)
    if (!std::strcmp(key, "_ZN7QWidget16contextMenuEventEP17QContextMenuEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_CONTEXTMENU)
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWidget11tabletEventEP12QTabletEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
#if !defined(QT_NO_ACTION)
    if (!std::strcmp(key, "_ZN7QWidget11actionEventEP12QActionEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_ACTION)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN7QWidget9showEventEP10QShowEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget9hideEventEP10QHideEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget11changeEventEP6QEvent")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget16inputMethodEventEP17QInputMethodEvent")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QWidget16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWidget18focusNextPrevChildEb")) {
      taken[42] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[43] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[44] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[45] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[46] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[47] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[48] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::initializeGL()
  void initializeGL() override {
    if (taken[0]) {
      int handled = 0;
      CuteGLWidgetCall0 call = reinterpret_cast<CuteGLWidgetCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    GLWidget::initializeGL();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::paintGL()
  void paintGL() override {
    if (taken[1]) {
      int handled = 0;
      CuteGLWidgetCall1 call = reinterpret_cast<CuteGLWidgetCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    GLWidget::paintGL();
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::resizeGL(int width, int height)
  void resizeGL(int width, int height) override {
    if (taken[2]) {
      int handled = 0;
      CuteGLWidgetCall2 call = reinterpret_cast<CuteGLWidgetCall2>(taken[2]);
      call(this, width, height, &handled);
      if (handled) return;
    }
    GLWidget::resizeGL(width, height);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteGLWidgetCall3 call = reinterpret_cast<CuteGLWidgetCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    GLWidget::mouseDoubleClickEvent(event);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteGLWidgetCall4 call = reinterpret_cast<CuteGLWidgetCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    GLWidget::mouseMoveEvent(event);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteGLWidgetCall5 call = reinterpret_cast<CuteGLWidgetCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    GLWidget::mousePressEvent(event);
  }
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
  //  void GLWidget::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteGLWidgetCall6 call = reinterpret_cast<CuteGLWidgetCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    GLWidget::mouseReleaseEvent(event);
  }
#endif  // !defined(QT_NO_OPENGL)

  //  void QOpenGLWidget::paintEvent(QPaintEvent *e)
  void paintEvent(QPaintEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteGLWidgetCall7 call = reinterpret_cast<CuteGLWidgetCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QOpenGLWidget::paintEvent(e);
  }

  //  void QOpenGLWidget::resizeEvent(QResizeEvent *e)
  void resizeEvent(QResizeEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteGLWidgetCall8 call = reinterpret_cast<CuteGLWidgetCall8>(taken[8]);
      call(this, e, &handled);
      if (handled) return;
    }
    QOpenGLWidget::resizeEvent(e);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QOpenGLWidget::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[9]) {
      int handled = 0;
      CuteGLWidgetCall9 call = reinterpret_cast<CuteGLWidgetCall9>(taken[9]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QOpenGLWidget::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  int QOpenGLWidget::metric(QPaintDevice::PaintDeviceMetric metric)
  //      const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[10]) {
      int handled = 0;
      CuteGLWidgetCall10 call = reinterpret_cast<CuteGLWidgetCall10>(taken[10]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QOpenGLWidget::metric(metric);
  }

  //  QPaintDevice *QOpenGLWidget::redirected(QPoint *p) const
  QPaintDevice *redirected(QPoint *p) const override {
    if (taken[11]) {
      int handled = 0;
      CuteGLWidgetCall11 call = reinterpret_cast<CuteGLWidgetCall11>(taken[11]);
      void * given = call(this, p, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QOpenGLWidget::redirected(p);
  }

  //  QPaintEngine *QOpenGLWidget::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[12]) {
      int handled = 0;
      CuteGLWidgetCall12 call = reinterpret_cast<CuteGLWidgetCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QOpenGLWidget::paintEngine();
  }

  //  int QWidget::devType() const
  int devType() const override {
    if (taken[13]) {
      int handled = 0;
      CuteGLWidgetCall13 call = reinterpret_cast<CuteGLWidgetCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::devType();
  }

  //  void QWidget::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteGLWidgetCall14 call = reinterpret_cast<CuteGLWidgetCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QWidget::setVisible(visible);
  }

  //  QSize QWidget::sizeHint() const
  QSize sizeHint() const override {
    if (taken[15]) {
      int handled = 0;
      CuteGLWidgetCall15 call = reinterpret_cast<CuteGLWidgetCall15>(taken[15]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::sizeHint();
  }

  //  QSize QWidget::minimumSizeHint() const
  QSize minimumSizeHint() const override {
    if (taken[16]) {
      int handled = 0;
      CuteGLWidgetCall16 call = reinterpret_cast<CuteGLWidgetCall16>(taken[16]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidget::minimumSizeHint();
  }

  //  int QWidget::heightForWidth(int a0) const
  int heightForWidth(int a0) const override {
    if (taken[17]) {
      int handled = 0;
      CuteGLWidgetCall17 call = reinterpret_cast<CuteGLWidgetCall17>(taken[17]);
      int given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidget::heightForWidth(a0);
  }

  //  bool QWidget::hasHeightForWidth() const
  bool hasHeightForWidth() const override {
    if (taken[18]) {
      int handled = 0;
      CuteGLWidgetCall18 call = reinterpret_cast<CuteGLWidgetCall18>(taken[18]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidget::hasHeightForWidth();
  }

#if QT_CONFIG(wheelevent)
  //  void QWidget::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteGLWidgetCall19 call = reinterpret_cast<CuteGLWidgetCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWidget::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteGLWidgetCall20 call = reinterpret_cast<CuteGLWidgetCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyPressEvent(event);
  }

  //  void QWidget::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteGLWidgetCall21 call = reinterpret_cast<CuteGLWidgetCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::keyReleaseEvent(event);
  }

  //  void QWidget::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteGLWidgetCall22 call = reinterpret_cast<CuteGLWidgetCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusInEvent(event);
  }

  //  void QWidget::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteGLWidgetCall23 call = reinterpret_cast<CuteGLWidgetCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::focusOutEvent(event);
  }

  //  void QWidget::enterEvent(QEnterEvent *event)
  void enterEvent(QEnterEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteGLWidgetCall24 call = reinterpret_cast<CuteGLWidgetCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::enterEvent(event);
  }

  //  void QWidget::leaveEvent(QEvent *event)
  void leaveEvent(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteGLWidgetCall25 call = reinterpret_cast<CuteGLWidgetCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::leaveEvent(event);
  }

  //  void QWidget::moveEvent(QMoveEvent *event)
  void moveEvent(QMoveEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteGLWidgetCall26 call = reinterpret_cast<CuteGLWidgetCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::moveEvent(event);
  }

  //  void QWidget::closeEvent(QCloseEvent *event)
  void closeEvent(QCloseEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteGLWidgetCall27 call = reinterpret_cast<CuteGLWidgetCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::closeEvent(event);
  }

#if !defined(QT_NO_CONTEXTMENU)
  //  void QWidget::contextMenuEvent(QContextMenuEvent *event)
  void contextMenuEvent(QContextMenuEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteGLWidgetCall28 call = reinterpret_cast<CuteGLWidgetCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::contextMenuEvent(event);
  }
#endif  // !defined(QT_NO_CONTEXTMENU)

#if QT_CONFIG(tabletevent)
  //  void QWidget::tabletEvent(QTabletEvent *event)
  void tabletEvent(QTabletEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteGLWidgetCall29 call = reinterpret_cast<CuteGLWidgetCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::tabletEvent(event);
  }
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_ACTION)
  //  void QWidget::actionEvent(QActionEvent *event)
  void actionEvent(QActionEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteGLWidgetCall30 call = reinterpret_cast<CuteGLWidgetCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::actionEvent(event);
  }
#endif  // !defined(QT_NO_ACTION)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragEnterEvent(QDragEnterEvent *event)
  void dragEnterEvent(QDragEnterEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteGLWidgetCall31 call = reinterpret_cast<CuteGLWidgetCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragEnterEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragMoveEvent(QDragMoveEvent *event)
  void dragMoveEvent(QDragMoveEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteGLWidgetCall32 call = reinterpret_cast<CuteGLWidgetCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragMoveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dragLeaveEvent(QDragLeaveEvent *event)
  void dragLeaveEvent(QDragLeaveEvent *event) override {
    if (taken[33]) {
      int handled = 0;
      CuteGLWidgetCall33 call = reinterpret_cast<CuteGLWidgetCall33>(taken[33]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dragLeaveEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
  //  void QWidget::dropEvent(QDropEvent *event)
  void dropEvent(QDropEvent *event) override {
    if (taken[34]) {
      int handled = 0;
      CuteGLWidgetCall34 call = reinterpret_cast<CuteGLWidgetCall34>(taken[34]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::dropEvent(event);
  }
#endif  // QT_CONFIG(draganddrop)

  //  void QWidget::showEvent(QShowEvent *event)
  void showEvent(QShowEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteGLWidgetCall35 call = reinterpret_cast<CuteGLWidgetCall35>(taken[35]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::showEvent(event);
  }

  //  void QWidget::hideEvent(QHideEvent *event)
  void hideEvent(QHideEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteGLWidgetCall36 call = reinterpret_cast<CuteGLWidgetCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QWidget::hideEvent(event);
  }

  //  void QWidget::changeEvent(QEvent *a0)
  void changeEvent(QEvent *a0) override {
    if (taken[37]) {
      int handled = 0;
      CuteGLWidgetCall37 call = reinterpret_cast<CuteGLWidgetCall37>(taken[37]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::changeEvent(a0);
  }

  //  void QWidget::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[38]) {
      int handled = 0;
      CuteGLWidgetCall38 call = reinterpret_cast<CuteGLWidgetCall38>(taken[38]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QWidget::initPainter(painter);
  }

  //  QPainter *QWidget::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[39]) {
      int handled = 0;
      CuteGLWidgetCall39 call = reinterpret_cast<CuteGLWidgetCall39>(taken[39]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QWidget::sharedPainter();
  }

  //  void QWidget::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteGLWidgetCall40 call = reinterpret_cast<CuteGLWidgetCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidget::inputMethodEvent(a0);
  }

  //  QVariant QWidget::inputMethodQuery(Qt::InputMethodQuery a0) const
  QVariant inputMethodQuery(Qt::InputMethodQuery a0) const override {
    if (taken[41]) {
      int handled = 0;
      CuteGLWidgetCall41 call = reinterpret_cast<CuteGLWidgetCall41>(taken[41]);
      const QVariant * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) return *given;
    }
    return QWidget::inputMethodQuery(a0);
  }

  //  bool QWidget::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[42]) {
      int handled = 0;
      CuteGLWidgetCall42 call = reinterpret_cast<CuteGLWidgetCall42>(taken[42]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QWidget::focusNextPrevChild(next);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[43]) {
      int handled = 0;
      CuteGLWidgetCall43 call = reinterpret_cast<CuteGLWidgetCall43>(taken[43]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[44]) {
      int handled = 0;
      CuteGLWidgetCall44 call = reinterpret_cast<CuteGLWidgetCall44>(taken[44]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[45]) {
      int handled = 0;
      CuteGLWidgetCall45 call = reinterpret_cast<CuteGLWidgetCall45>(taken[45]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[46]) {
      int handled = 0;
      CuteGLWidgetCall46 call = reinterpret_cast<CuteGLWidgetCall46>(taken[46]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[47]) {
      int handled = 0;
      CuteGLWidgetCall47 call = reinterpret_cast<CuteGLWidgetCall47>(taken[47]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[48]) {
      int handled = 0;
      CuteGLWidgetCall48 call = reinterpret_cast<CuteGLWidgetCall48>(taken[48]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *GLWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK8GLWidget10metaObjectEv(const GLWidget *self) {
  return self->metaObject();
}

//  void *GLWidget::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN8GLWidget11qt_metacastEPKc(GLWidget *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int GLWidget::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN8GLWidget11qt_metacallEN11QMetaObject4CallEiPPv(
    GLWidget *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

#if !defined(QT_NO_OPENGL)
//  QString GLWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8GLWidget2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(GLWidget::tr(s, c, n));
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  GLWidget::GLWidget(GLXYSeriesDataManager *xyDataManager, QChart *chart,
//      QGraphicsView *parent)
extern "C" Q_DECL_EXPORT
GLWidget *ritual_ZN8GLWidgetC1EP21GLXYSeriesDataManagerP6QChartP13QGraphicsView(
    GLXYSeriesDataManager *xyDataManager,
    QChart *chart,
    QGraphicsView *parent) {
  return new CuteGLWidget(xyDataManager, chart, parent);
}
#endif  // !defined(QT_NO_OPENGL)

//  GLWidget::~GLWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidgetD1Ev(GLWidget *self) {
  delete self;
}

#if !defined(QT_NO_OPENGL)
//  bool GLWidget::needsReset() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8GLWidget10needsResetEv(const GLWidget *self) {
  return self->needsReset();
}
#endif  // !defined(QT_NO_OPENGL)

//  void GLWidget::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget7cleanupEv(GLWidget *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "GLWidget")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cleanup()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cleanup()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void GLWidget::cleanXYSeriesResources(const QXYSeries *series)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget22cleanXYSeriesResourcesEPK9QXYSeries(
    GLWidget *self,
    const QXYSeries *series) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "GLWidget")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cleanXYSeriesResources(const QXYSeries *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cleanXYSeriesResources(const QXYSeries *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&series)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void GLWidget::initializeGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget12initializeGLEv(GLWidget *self) {
  self->initializeGL();
}

//  void GLWidget::paintGL()
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget7paintGLEv(GLWidget *self) {
  self->paintGL();
}

//  void GLWidget::resizeGL(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget8resizeGLEii(GLWidget *self, int width, int height) {
  self->resizeGL(width, height);
}

//  void GLWidget::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget21mouseDoubleClickEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void GLWidget::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget14mouseMoveEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void GLWidget::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget15mousePressEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void GLWidget::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget17mouseReleaseEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

#if !defined(QT_NO_OPENGL)
//  QXYSeries *GLWidget::findSeriesAtEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN8GLWidget17findSeriesAtEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  return self->findSeriesAtEvent(event);
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::render(bool selection)
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget6renderEb(GLWidget *self, bool selection) {
  self->render(selection);
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::recreateSelectionFbo()
extern "C" Q_DECL_EXPORT
void ritual_ZN8GLWidget20recreateSelectionFboEv(GLWidget *self) {
  self->recreateSelectionFbo();
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  QXYSeries *GLWidget::chartSeries(const QXYSeries *cSeries)
extern "C" Q_DECL_EXPORT
QXYSeries *ritual_ZN8GLWidget11chartSeriesEPK9QXYSeries(
    GLWidget *self,
    const QXYSeries *cSeries) {
  return self->chartSeries(cSeries);
}
#endif  // !defined(QT_NO_OPENGL)

//  GLWidget as the QOpenGLFunctions it is built on
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_cast_GLWidget_QOpenGLFunctions(GLWidget *self) {
  return static_cast<QOpenGLFunctions *>(self);
}

//  a Python function taken by a CuteGLWidget, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_GLWidget(GLWidget *self, const char *key, void *call) {
  return static_cast<CuteGLWidget *>(self)->take(key, call);
}

#if !defined(QT_NO_OPENGL)
//  void GLWidget::initializeGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget12initializeGLEv(GLWidget *self) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::initializeGL();
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::paintGL()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget7paintGLEv(GLWidget *self) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::paintGL();
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::resizeGL(int width, int height)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget8resizeGLEii(
    GLWidget *self,
    int width,
    int height) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::resizeGL(width, height);
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget21mouseDoubleClickEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::mouseDoubleClickEvent(
      event);
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget14mouseMoveEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::mouseMoveEvent(event);
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget15mousePressEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::mousePressEvent(event);
}
#endif  // !defined(QT_NO_OPENGL)

#if !defined(QT_NO_OPENGL)
//  void GLWidget::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8GLWidget17mouseReleaseEventEP11QMouseEvent(
    GLWidget *self,
    QMouseEvent *event) {
  static_cast<OwnGLWidget *>(self)->OwnGLWidget::mouseReleaseEvent(event);
}
#endif  // !defined(QT_NO_OPENGL)

#endif  // !defined(QT_NO_OPENGL)
#endif  // QT_CONFIG(opengl)
