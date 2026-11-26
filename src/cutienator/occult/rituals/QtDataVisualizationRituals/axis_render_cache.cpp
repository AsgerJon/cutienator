//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/axisrendercache_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for 'AxisRenderCache' is
//  pasted in, cut from what the moc of Qt 6.12.0 writes for its header: Qt's
//  library keeps it to itself; added are 2 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/axisrendercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtDataVisualization/private/axisrendercache_p.h>
#include <QtGui/QFontMetrics>
#include <QtDataVisualization/private/labelitem_p.h>
#include <QtDataVisualization/private/drawer_p.h>
#include <QtDataVisualization/private/shaderhelper_p.h>
#include <QtDataVisualization/private/surfaceobject_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/abstract3drenderer_p.h>
#include <QtDataVisualization/private/scatterpointbufferhelper_p.h>
#include <QtGui/QMatrix4x4>
#include <QtGui/qquaternion.h>
#include <QtCore/qmath.h>
#include <QtDataVisualization/private/texturehelper_p.h>
#include <QtDataVisualization/private/utils_p.h>
#include <QtGui/QImage>
#include <QtGui/QPainter>
#include <QtCore/QTime>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from QtDataVisualization__AxisRenderCache.cpp, line 1, as moc:AxisRenderCache
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN15AxisRenderCacheE_t {};
} // unnamed namespace

template <> constexpr inline auto AxisRenderCache::qt_create_metaobjectdata<qt_meta_tag_ZN15AxisRenderCacheE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "AxisRenderCache"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<AxisRenderCache, qt_meta_tag_ZN15AxisRenderCacheE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject AxisRenderCache::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15AxisRenderCacheE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15AxisRenderCacheE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN15AxisRenderCacheE_t>.metaTypes,
    nullptr
} };

void AxisRenderCache::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<AxisRenderCache *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *AxisRenderCache::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *AxisRenderCache::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN15AxisRenderCacheE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int AxisRenderCache::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 32, as _ZN15AxisRenderCacheD0Ev
inline AxisRenderCache::~AxisRenderCache()
{
    for (auto label: m_labelItems)
        delete label;
    m_titleItem.clear();

    delete m_formatter;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 8, as _ZN9LabelItemC1Ev
inline LabelItem::LabelItem()
    : m_size(QSize(0, 0)),
      m_textureId(0)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 407, as _ZN6Drawer17generateLabelItemER9LabelItemRK7QStringi
inline void Drawer::generateLabelItem(LabelItem &item, const QString &text, int widestLabel)
{
    initializeOpenGL();

    item.clear();

    if (!text.isEmpty()) {
        // Create labels
        // Print label into a QImage using QPainter
        QImage label = Utils::printTextToImage(m_theme->font(),
                                               text,
                                               m_theme->labelBackgroundColor(),
                                               m_theme->labelTextColor(),
                                               m_theme->isLabelBackgroundEnabled(),
                                               m_theme->isLabelBorderEnabled(),
                                               widestLabel);

        // Set label size
        item.setSize(label.size());
        // Insert text texture into label (also deletes the old texture)
        item.setTextureId(m_textureHelper->create2DTexture(label, true, true));
    }
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 40, as _ZN9LabelItem5clearEv
inline void LabelItem::clear()
{
    if (m_textureId && QOpenGLContext::currentContext())
        QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = 0;
    m_size = QSize(0, 0);
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 73, as _ZNK6Drawer4fontEv
inline QFont Drawer::font() const
{
    return m_theme->font();
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 14, as _ZN9LabelItemD1Ev
inline LabelItem::~LabelItem()
{
    clear();
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 24, as _ZNK9LabelItem4sizeEv
inline QSize LabelItem::size() const
{
    return m_size;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 44, as _ZN13TextureHelper15create2DTextureERK6QImagebbbb
inline GLuint TextureHelper::create2DTexture(const QImage &image, bool useTrilinearFiltering,
                                      bool convert, bool smoothScale, bool clampY)
{
    if (image.isNull())
        return 0;

    QImage texImage = image;

    if (Utils::isOpenGLES()) {
        GLuint imageWidth = Utils::getNearestPowerOfTwo(image.width());
        GLuint imageHeight = Utils::getNearestPowerOfTwo(image.height());
        if (smoothScale) {
            texImage = image.scaled(imageWidth, imageHeight, Qt::IgnoreAspectRatio,
                                    Qt::SmoothTransformation);
        } else {
            texImage = image.scaled(imageWidth, imageHeight, Qt::IgnoreAspectRatio);
        }
    }

    GLuint textureId;
    glGenTextures(1, &textureId);
    glBindTexture(GL_TEXTURE_2D, textureId);
    if (convert)
        texImage = convertToGLFormat(texImage);
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, texImage.width(), texImage.height(),
                 0, GL_RGBA, GL_UNSIGNED_BYTE, texImage.bits());
    if (smoothScale)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    else
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    if (useTrilinearFiltering) {
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);
        glGenerateMipmap(GL_TEXTURE_2D);
    } else {
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    }
    if (clampY)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
    glBindTexture(GL_TEXTURE_2D, 0);

    return textureId;
}

//  from ../qtdatavis3d/src/datavisualization/engine/drawer.cpp, line 54, as _ZN6Drawer16initializeOpenGLEv
inline void Drawer::initializeOpenGL()
{
    initializeOpenGLFunctions();
    if (!m_textureHelper)
        m_textureHelper = new TextureHelper();
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 29, as _ZN9LabelItem12setTextureIdEj
inline void LabelItem::setTextureId(GLuint textureId)
{
    QOpenGLContext::currentContext()->functions()->glDeleteTextures(1, &m_textureId);
    m_textureId = textureId;
}

//  from ../qtdatavis3d/src/datavisualization/data/labelitem.cpp, line 19, as _ZN9LabelItem7setSizeERK5QSize
inline void LabelItem::setSize(const QSize &size)
{
    m_size = size;
}

//  from ../qtdatavis3d/src/datavisualization/utils/texturehelper.cpp, line 334, as _ZN13TextureHelper17convertToGLFormatERK6QImage
inline QImage TextureHelper::convertToGLFormat(const QImage &srcImage)
{
    QImage res(srcImage.size(), QImage::Format_ARGB32);
    convertToGLFormatHelper(res, srcImage.convertToFormat(QImage::Format_ARGB32), GL_RGBA);
    return res;
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 12, as _ZN15AxisRenderCacheC1Ev
inline AxisRenderCache::AxisRenderCache()
    : m_type(QAbstract3DAxis::AxisTypeNone),
      m_min(0.0f),
      m_max(10.0f),
      m_segmentCount(5),
      m_subSegmentCount(1),
      m_reversed(false),
      m_font(QFont(QStringLiteral("Arial"))),
      m_formatter(0),
      m_ctrlFormatter(0),
      m_drawer(0),
      m_positionsDirty(true),
      m_translate(0.0f),
      m_scale(1.0f),
      m_labelAutoRotation(0.0f),
      m_titleVisible(false),
      m_titleFixed(false)
{
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 49, as _ZN15AxisRenderCache7setTypeEN15QAbstract3DAxis8AxisTypeE
inline void AxisRenderCache::setType(QAbstract3DAxis::AxisType type)
{
    m_type = type;

    // If type is set, it means completely new axis instance, so clear all old data
    m_labels.clear();
    m_title.clear();
    m_min = 0.0f;
    m_max = 10.0f;
    m_segmentCount = 5;
    m_subSegmentCount = 1;
    m_labelFormat.clear();

    m_titleItem.clear();
    for (auto label: m_labelItems)
        delete label;
    m_labelItems.clear();
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 107, as _ZN15AxisRenderCache18updateAllPositionsEv
inline void AxisRenderCache::updateAllPositions()
{
    // As long as grid and subgrid lines are drawn identically, we can further optimize
    // by caching all grid and subgrid positions into a single list.
    // If subgrid lines are ever themed separately, this array will probably become obsolete.
    if (m_formatter) {
        int gridCount = m_formatter->gridPositions().size();
        int subGridCount = m_formatter->subGridPositions().size();
        int labelCount = m_formatter->labelPositions().size();
        int fullSize = gridCount + subGridCount;

        m_adjustedGridLinePositions.resize(fullSize);
        m_adjustedLabelPositions.resize(labelCount);
        int index = 0;
        int grid = 0;
        int label = 0;
        float position = 0.0f;
        for (; label < labelCount; label++) {
            position = m_formatter->labelPositions().at(label);
            if (m_reversed)
                position = 1.0f - position;
            m_adjustedLabelPositions[label] = position * m_scale + m_translate;
        }
        for (; grid < gridCount; grid++) {
            position = m_formatter->gridPositions().at(grid);
            if (m_reversed)
                position = 1.0f - position;
            m_adjustedGridLinePositions[index++] = position * m_scale + m_translate;
        }
        for (int subGrid = 0; subGrid < subGridCount; subGrid++) {
            position = m_formatter->subGridPositions().at(subGrid);
            if (m_reversed)
                position = 1.0f - position;
            m_adjustedGridLinePositions[index++] = position * m_scale + m_translate;
        }

        m_positionsDirty = false;
    }
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 166, as _ZN15AxisRenderCache11clearLabelsEv
inline void AxisRenderCache::clearLabels()
{
    m_titleItem.clear();
    for (int i = 0; i < m_labels.size(); i++)
        m_labelItems[i]->clear();
}

//  from ../qtdatavis3d/src/datavisualization/engine/axisrendercache.cpp, line 173, as _ZNK15AxisRenderCache13maxLabelWidthERK5QListI7QStringE
inline int AxisRenderCache::maxLabelWidth(const QStringList &labels) const
{
    int labelWidth = 0;
    QFont labelFont = m_font;
    labelFont.setPointSize(textureFontSize);
    QFontMetrics labelFM(labelFont);
    for (int i = 0; i < labels.size(); i++) {
        int newWidth = labelFM.horizontalAdvance(labels.at(i));
        if (labelWidth < newWidth)
            labelWidth = newWidth;
    }
    return labelWidth;
}
//  -----------------------------------------------------------------------

//  A AxisRenderCache that Python can take functions over in. Every AxisRenderCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisRenderCacheCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteAxisRenderCacheCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRenderCacheCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRenderCacheCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRenderCacheCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRenderCacheCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteAxisRenderCacheCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteAxisRenderCache : public AxisRenderCache {
public:
  using AxisRenderCache::AxisRenderCache;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteAxisRenderCacheCall0 call = reinterpret_cast<CuteAxisRenderCacheCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteAxisRenderCacheCall1 call = reinterpret_cast<CuteAxisRenderCacheCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteAxisRenderCacheCall2 call = reinterpret_cast<CuteAxisRenderCacheCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteAxisRenderCacheCall3 call = reinterpret_cast<CuteAxisRenderCacheCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteAxisRenderCacheCall4 call = reinterpret_cast<CuteAxisRenderCacheCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteAxisRenderCacheCall5 call = reinterpret_cast<CuteAxisRenderCacheCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteAxisRenderCacheCall6 call = reinterpret_cast<CuteAxisRenderCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *AxisRenderCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15AxisRenderCache10metaObjectEv(
    const AxisRenderCache *self) {
  return self->metaObject();
}

//  void *AxisRenderCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15AxisRenderCache11qt_metacastEPKc(
    AxisRenderCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int AxisRenderCache::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15AxisRenderCache11qt_metacallEN11QMetaObject4CallEiPPv(
    AxisRenderCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString AxisRenderCache::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15AxisRenderCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(AxisRenderCache::tr(s, c, n));
}

//  AxisRenderCache::AxisRenderCache()
extern "C" Q_DECL_EXPORT
AxisRenderCache *ritual_ZN15AxisRenderCacheC1Ev() {
  return new CuteAxisRenderCache();
}

//  AxisRenderCache::~AxisRenderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCacheD1Ev(AxisRenderCache *self) {
  delete self;
}

//  void AxisRenderCache::setType(QAbstract3DAxis::AxisType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache7setTypeEN15QAbstract3DAxis8AxisTypeE(
    AxisRenderCache *self,
    QAbstract3DAxis::AxisType type) {
  self->setType(type);
}

//  QAbstract3DAxis::AxisType AxisRenderCache::type() const
extern "C" Q_DECL_EXPORT
QAbstract3DAxis::AxisType ritual_ZNK15AxisRenderCache4typeEv(
    const AxisRenderCache *self) {
  return self->type();
}

//  const QString &AxisRenderCache::title() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15AxisRenderCache5titleEv(const AxisRenderCache *self) {
  return new QString(self->title());
}

//  const QStringList &AxisRenderCache::labels() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15AxisRenderCache6labelsEv(
    const AxisRenderCache *self) {
  return new QList<QString>(self->labels());
}

//  void AxisRenderCache::setMin(float min)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache6setMinEf(AxisRenderCache *self, float min) {
  self->setMin(min);
}

//  float AxisRenderCache::min() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15AxisRenderCache3minEv(const AxisRenderCache *self) {
  return self->min();
}

//  void AxisRenderCache::setMax(float max)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache6setMaxEf(AxisRenderCache *self, float max) {
  self->setMax(max);
}

//  float AxisRenderCache::max() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15AxisRenderCache3maxEv(const AxisRenderCache *self) {
  return self->max();
}

//  void AxisRenderCache::setSegmentCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache15setSegmentCountEi(
    AxisRenderCache *self,
    int count) {
  self->setSegmentCount(count);
}

//  int AxisRenderCache::segmentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15AxisRenderCache12segmentCountEv(
    const AxisRenderCache *self) {
  return self->segmentCount();
}

//  void AxisRenderCache::setSubSegmentCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache18setSubSegmentCountEi(
    AxisRenderCache *self,
    int count) {
  self->setSubSegmentCount(count);
}

//  int AxisRenderCache::subSegmentCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15AxisRenderCache15subSegmentCountEv(
    const AxisRenderCache *self) {
  return self->subSegmentCount();
}

//  void AxisRenderCache::setLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache14setLabelFormatERK7QString(
    AxisRenderCache *self,
    const QString *format) {
  self->setLabelFormat(*format);
}

//  const QString &AxisRenderCache::labelFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15AxisRenderCache11labelFormatEv(
    const AxisRenderCache *self) {
  return new QString(self->labelFormat());
}

//  void AxisRenderCache::setReversed(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache11setReversedEb(
    AxisRenderCache *self,
    bool enable) {
  self->setReversed(enable);
}

//  bool AxisRenderCache::reversed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15AxisRenderCache8reversedEv(const AxisRenderCache *self) {
  return self->reversed();
}

//  void AxisRenderCache::setFormatter(QValue3DAxisFormatter *formatter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache12setFormatterEP21QValue3DAxisFormatter(
    AxisRenderCache *self,
    QValue3DAxisFormatter *formatter) {
  self->setFormatter(formatter);
}

//  QValue3DAxisFormatter *AxisRenderCache::formatter() const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZNK15AxisRenderCache9formatterEv(
    const AxisRenderCache *self) {
  return self->formatter();
}

//  void AxisRenderCache::setCtrlFormatter(QValue3DAxisFormatter *formatter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache16setCtrlFormatterEP21QValue3DAxisFormatter(
    AxisRenderCache *self,
    QValue3DAxisFormatter *formatter) {
  self->setCtrlFormatter(formatter);
}

//  QValue3DAxisFormatter *AxisRenderCache::ctrlFormatter() const
extern "C" Q_DECL_EXPORT
QValue3DAxisFormatter *ritual_ZNK15AxisRenderCache13ctrlFormatterEv(
    const AxisRenderCache *self) {
  return self->ctrlFormatter();
}

//  LabelItem &AxisRenderCache::titleItem()
extern "C" Q_DECL_EXPORT
LabelItem *ritual_ZN15AxisRenderCache9titleItemEv(AxisRenderCache *self) {
  return &(self->titleItem());
}

//  QList<LabelItem *> &AxisRenderCache::labelItems()
extern "C" Q_DECL_EXPORT
QList<LabelItem *> *ritual_ZN15AxisRenderCache10labelItemsEv(
    AxisRenderCache *self) {
  return &(self->labelItems());
}

//  float AxisRenderCache::gridLinePosition(int index)
extern "C" Q_DECL_EXPORT
float ritual_ZN15AxisRenderCache16gridLinePositionEi(
    AxisRenderCache *self,
    int index) {
  return self->gridLinePosition(index);
}

//  int AxisRenderCache::gridLineCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN15AxisRenderCache13gridLineCountEv(AxisRenderCache *self) {
  return self->gridLineCount();
}

//  float AxisRenderCache::labelPosition(int index)
extern "C" Q_DECL_EXPORT
float ritual_ZN15AxisRenderCache13labelPositionEi(
    AxisRenderCache *self,
    int index) {
  return self->labelPosition(index);
}

//  int AxisRenderCache::labelCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN15AxisRenderCache10labelCountEv(AxisRenderCache *self) {
  return self->labelCount();
}

//  void AxisRenderCache::updateAllPositions()
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache18updateAllPositionsEv(
    AxisRenderCache *self) {
  self->updateAllPositions();
}

//  bool AxisRenderCache::positionsDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15AxisRenderCache14positionsDirtyEv(
    const AxisRenderCache *self) {
  return self->positionsDirty();
}

//  void AxisRenderCache::markPositionsDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache18markPositionsDirtyEv(
    AxisRenderCache *self) {
  self->markPositionsDirty();
}

//  void AxisRenderCache::setTranslate(float translate)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache12setTranslateEf(
    AxisRenderCache *self,
    float translate) {
  self->setTranslate(translate);
}

//  float AxisRenderCache::translate()
extern "C" Q_DECL_EXPORT
float ritual_ZN15AxisRenderCache9translateEv(AxisRenderCache *self) {
  return self->translate();
}

//  void AxisRenderCache::setScale(float scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache8setScaleEf(
    AxisRenderCache *self,
    float scale) {
  self->setScale(scale);
}

//  float AxisRenderCache::scale()
extern "C" Q_DECL_EXPORT
float ritual_ZN15AxisRenderCache5scaleEv(AxisRenderCache *self) {
  return self->scale();
}

//  float AxisRenderCache::positionAt(float value)
extern "C" Q_DECL_EXPORT
float ritual_ZN15AxisRenderCache10positionAtEf(
    AxisRenderCache *self,
    float value) {
  return self->positionAt(value);
}

//  float AxisRenderCache::labelAutoRotation() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15AxisRenderCache17labelAutoRotationEv(
    const AxisRenderCache *self) {
  return self->labelAutoRotation();
}

//  void AxisRenderCache::setLabelAutoRotation(float angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache20setLabelAutoRotationEf(
    AxisRenderCache *self,
    float angle) {
  self->setLabelAutoRotation(angle);
}

//  bool AxisRenderCache::isTitleVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15AxisRenderCache14isTitleVisibleEv(
    const AxisRenderCache *self) {
  return self->isTitleVisible();
}

//  void AxisRenderCache::setTitleVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache15setTitleVisibleEb(
    AxisRenderCache *self,
    bool visible) {
  self->setTitleVisible(visible);
}

//  bool AxisRenderCache::isTitleFixed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15AxisRenderCache12isTitleFixedEv(
    const AxisRenderCache *self) {
  return self->isTitleFixed();
}

//  void AxisRenderCache::setTitleFixed(bool fixed)
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache13setTitleFixedEb(
    AxisRenderCache *self,
    bool fixed) {
  self->setTitleFixed(fixed);
}

//  void AxisRenderCache::clearLabels()
extern "C" Q_DECL_EXPORT
void ritual_ZN15AxisRenderCache11clearLabelsEv(AxisRenderCache *self) {
  self->clearLabels();
}

//  int AxisRenderCache::maxLabelWidth(const QStringList &labels) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15AxisRenderCache13maxLabelWidthERK5QListI7QStringE(
    const AxisRenderCache *self,
    const QList<QString> *labels) {
  return self->maxLabelWidth(*labels);
}

//  a Python function taken by a CuteAxisRenderCache, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AxisRenderCache(
    AxisRenderCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteAxisRenderCache *>(self)->take(key, call);
}
