//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h, Qt 6.12.0, as the Qt
//  of macOS and the Qt of Windows install it. Kept as it is when the
//  generator runs again. Its header needs FreeType's, which these
//  two install with Qt's, in the folder 'QtFreetype'.
//  FreeType's faces and glyph slots are passed as addresses, its
//  'FT_Fixed' as a 'long'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype)
#include <QtGui/6.12.0/QtGui/private/qfontengine_ft_p.h>
#include <QtGui/qfontvariableaxis.h>
#include <QtGui/qpainterpath.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>

//  QFreetypeFace::QFreetypeFace()
extern "C" Q_DECL_EXPORT
QFreetypeFace *ritual_ZN13QFreetypeFaceC1Ev() {
  return new QFreetypeFace();
}

//  QFreetypeFace::~QFreetypeFace()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFaceD1Ev(QFreetypeFace *self) {
  delete self;
}

//  void QFreetypeFace::computeSize(const QFontDef &fontDef, int *xsize, int
//      *ysize, bool *outline_drawing, QFixed *scalableBitmapScaleFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace11computeSizeERK8QFontDefPiS3_PbP6QFixed(
    QFreetypeFace *self,
    const QFontDef *fontDef,
    int *xsize,
    int *ysize,
    bool *outline_drawing,
    QFixed *scalableBitmapScaleFactor) {
  self->computeSize(*fontDef, xsize, ysize, outline_drawing, scalableBitmapScaleFactor);
}

//  QFontEngine::Properties QFreetypeFace::properties() const
extern "C" Q_DECL_EXPORT
QFontEngine::Properties *ritual_ZNK13QFreetypeFace10propertiesEv(
    const QFreetypeFace *self) {
  return new QFontEngine::Properties(self->properties());
}

//  bool QFreetypeFace::getSfntTable(uint tag, uchar *buffer, uint *length)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFreetypeFace12getSfntTableEjPhPj(
    const QFreetypeFace *self,
    uint tag,
    uchar *buffer,
    uint *length) {
  return self->getSfntTable(tag, buffer, length);
}

//  QFreetypeFace *QFreetypeFace::getFace(const QFontEngine::FaceId &face_id,
//      const QByteArray &fontData)
extern "C" Q_DECL_EXPORT
QFreetypeFace *ritual_ZN13QFreetypeFace7getFaceERKN11QFontEngine6FaceIdERK10QByteArray(
    const QFontEngine::FaceId *face_id,
    const QByteArray *fontData) {
  return QFreetypeFace::getFace(*face_id, *fontData);
}

//  void QFreetypeFace::release(const QFontEngine::FaceId &face_id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace7releaseERKN11QFontEngine6FaceIdE(
    QFreetypeFace *self,
    const QFontEngine::FaceId *face_id) {
  self->release(*face_id);
}

//  int QFreetypeFace::getFaceIndexByStyleName(const QString &faceFileName,
//      const QString &styleName)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFreetypeFace23getFaceIndexByStyleNameERK7QStringS2_(
    const QString *faceFileName,
    const QString *styleName) {
  return QFreetypeFace::getFaceIndexByStyleName(*faceFileName, *styleName);
}

//  void QFreetypeFace::lock()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace4lockEv(QFreetypeFace *self) {
  self->lock();
}

//  void QFreetypeFace::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace6unlockEv(QFreetypeFace *self) {
  self->unlock();
}

//  int QFreetypeFace::fsType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFreetypeFace6fsTypeEv(const QFreetypeFace *self) {
  return self->fsType();
}

//  int QFreetypeFace::getPointInOutline(glyph_t glyph, int flags, quint32
//      point, QFixed *xpos, QFixed *ypos, quint32 *nPoints)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QFreetypeFace17getPointInOutlineEjijP6QFixedS1_Pj(
    QFreetypeFace *self,
    glyph_t glyph,
    int flags,
    quint32 point,
    QFixed *xpos,
    QFixed *ypos,
    quint32 *nPoints) {
  return self->getPointInOutline(glyph, flags, point, xpos, ypos, nPoints);
}

//  bool QFreetypeFace::isScalableBitmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFreetypeFace16isScalableBitmapEv(
    const QFreetypeFace *self) {
  return self->isScalableBitmap();
}

//  void QFreetypeFace::addGlyphToPath(FT_Face face, FT_GlyphSlot g, const
//      QFixedPoint &point, QPainterPath *path, FT_Fixed x_scale, FT_Fixed
//      y_scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace14addGlyphToPathEP11FT_FaceRec_P16FT_GlyphSlotRec_RK11QFixedPointP12QPainterPathll(
    FT_Face face,
    FT_GlyphSlot g,
    const QFixedPoint *point,
    QPainterPath *path,
    FT_Fixed x_scale,
    FT_Fixed y_scale) {
  QFreetypeFace::addGlyphToPath(face, g, *point, path, x_scale, y_scale);
}

//  void QFreetypeFace::addBitmapToPath(FT_GlyphSlot slot, const QFixedPoint
//      &point, QPainterPath *path)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace15addBitmapToPathEP16FT_GlyphSlotRec_RK11QFixedPointP12QPainterPath(
    FT_GlyphSlot slot,
    const QFixedPoint *point,
    QPainterPath *path) {
  QFreetypeFace::addBitmapToPath(slot, *point, path);
}

//  QList<QFontVariableAxis> QFreetypeFace::variableAxes() const
extern "C" Q_DECL_EXPORT
QList<QFontVariableAxis> *ritual_ZNK13QFreetypeFace12variableAxesEv(
    const QFreetypeFace *self) {
  return new QList<QFontVariableAxis>(self->variableAxes());
}

//  void QFreetypeFace::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFreetypeFace7cleanupEv(QFreetypeFace *self) {
  self->cleanup();
}

#endif  // (defined(Q_OS_WIN) || defined(Q_OS_DARWIN)) && QT_CONFIG(freetype)
